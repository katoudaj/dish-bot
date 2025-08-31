import os
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage
import random

load_dotenv()
ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

menus = ["カレーライス", "ハンバーグ", "豚の生姜焼き", "サバの味噌煮", "オムライス"]
menu_today = random.choice(menus)

bot = LineBotApi(ACCESS_TOKEN)
bot.broadcast(TextSendMessage(text=f"今日のおすすめメニューは{menu_today}！"))
