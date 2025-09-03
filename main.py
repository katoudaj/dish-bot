import os, random, requests
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage

load_dotenv()
ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")

bot = LineBotApi(ACCESS_TOKEN)

def fetch_recipe():
    url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
    params = {"applicationId": RAKUTEN_APP_ID,
              "categoryId": 38} # 38は今日の献立のカテゴリID
    res = requests.get(url, params=params).json()
    return random.choice(res.get("result", []))

recipe = fetch_recipe()
text = f"今日のおすすめメニュー：\n{recipe['recipeTitle']}\n{recipe['recipeUrl']}"
#bot.broadcast(TextSendMessage(text=text))
