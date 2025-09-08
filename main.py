import os
from dotenv import load_dotenv
load_dotenv()
import random
random.seed()
from linebot import LineBotApi
from linebot.models import TextSendMessage

from config import EXEC_MODE

if EXEC_MODE == "development":
    from recipe_provider_dummy import DummyRecipeProvider as RecipeProvider
else:
    from recipe_provider import RecipeProvider

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def send_random_recipe(user_id: str = None):
    provider = RecipeProvider()
    recipes = provider.get_recipes()
    if not recipes:
        return
    recipe = random.choice(recipes)
    msg = f"今日のおすすめ: {recipe.title}\n{recipe.url}"

    if EXEC_MODE == "development":
        print(msg)
    else:
        if user_id:
            line_bot_api.push_message(user_id, TextSendMessage(text=msg))
        else:
            line_bot_api.broadcast(TextSendMessage(text=msg))

if __name__ == "__main__":
    user_id = os.getenv("USER_ID")  # 例: workflow_dispatch inputs -> env
    send_random_recipe(user_id)
