import os
from dotenv import load_dotenv
load_dotenv()
import random
random.seed()
from linebot import LineBotApi
from linebot.models import TextSendMessage

from config import EXEC_MODE
if EXEC_MODE == "debug":
    from recipe_provider_dummy import DummyRecipeProvider as RecipeProvider
else:
    from recipe_provider import RecipeProvider
    
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-m','--message', type=str, default=None, help='メッセージ内容')
parser.add_argument('-u','--user_id', type=str, default=None, help='ユーザーID')
args = parser.parse_args()

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

def main():
    # コマンドライン引数 > 環境変数
    message = args.message or os.getenv("MESSAGE")
    user_id = args.user_id or os.getenv("USER_ID")
    
    if message == "info":
        reply = f"User ID: {user_id or 'None'}"
        line_bot_api.push_message(user_id, TextSendMessage(text=reply))
        return
    
    send_random_recipe(user_id)

if __name__ == "__main__":
    main()
