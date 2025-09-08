import os
import json
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DUMMY_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "dummy_recipes.json")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def export_recipes():
    # Supabaseから全レシピ取得
    recipes = supabase.table("recipes").select("title,url").execute().data
    # 必要なフィールドだけ抽出
    data = [{"title": r["title"], "url": r["url"]} for r in recipes]
    # JSONファイルとして保存
    with open(DUMMY_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(data)} recipes to {DUMMY_DB_PATH}")

if __name__ == "__main__":
    export_recipes()