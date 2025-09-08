from dotenv import load_dotenv
load_dotenv()
import requests
from supabase import create_client, Client
import os
from base import BaseRecipeProvider
from models import Recipe
from typing import List

# 環境変数
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")

# クライアント初期化
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class RecipeProvider(BaseRecipeProvider):
    def get_recipes(self) -> List[Recipe]:
        self.dump_new_recipes() # 取得ついでに新しいレシピをDBに保存
        recipes = supabase.table("recipes").select("title,url").execute().data
        return [Recipe(title=r["title"], url=r["url"]) for r in recipes]

    def dump_new_recipes(self):
        url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
        params = {"applicationId": RAKUTEN_APP_ID, "categoryId": "38"} # 38は今日の献立のカテゴリID
        res = requests.get(url, params=params).json()

        for r in res.get("result", []):
            recipe_url = r["recipeUrl"]
            # 既存チェック
            existing = supabase.table("recipes").select("id").eq("url", recipe_url).execute().data
            if not existing:
                supabase.table("recipes").insert({
                    "title": r["recipeTitle"],
                    "url": recipe_url,
                }).execute()
