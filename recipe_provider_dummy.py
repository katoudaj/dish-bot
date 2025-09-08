from dotenv import load_dotenv
load_dotenv()
import requests
from supabase import create_client, Client
from base import BaseRecipeProvider
from models import Recipe
from typing import List
import json
import os

DUMMY_DB_PATH = os.path.join(os.path.dirname(__file__), "dummy_recipes.json")

class DummyRecipeProvider(BaseRecipeProvider):
    def get_recipes(self) -> List[Recipe]:
        # ダミーDB（JSONファイル）からレシピを読み込む
        with open(DUMMY_DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Recipe(**r) for r in data]

