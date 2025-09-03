import os
from dotenv import load_dotenv
load_dotenv()
import random
random.seed()
import requests
from supabase import create_client, Client
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 環境変数
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")

# クライアント初期化
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def fetch_and_store_recipes():
    url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
    params = {"applicationId": RAKUTEN_APP_ID, "categoryId": "38"} # 38は今日の献立のカテゴリID
    res = requests.get(url, params=params).json()

    for r in res["result"]:
        recipe_url = r["recipeUrl"]
        # 既存チェック
        existing = supabase.table("recipes").select("id").eq("url", recipe_url).execute().data
        if not existing:
            supabase.table("recipes").insert({
                "title": r["recipeTitle"],
                "url": recipe_url,
            }).execute()

def send_random_recipe():
    recipes = supabase.table("recipes").select("title,url").execute().data
    if not recipes:
        return
    recipe = random.choice(recipes)
    msg = f"今日のおすすめ: {recipe['title']}\n{recipe['url']}"
    line_bot_api.broadcast(TextSendMessage(text=msg))

if __name__ == "__main__":
    fetch_and_store_recipes()
    send_random_recipe()
