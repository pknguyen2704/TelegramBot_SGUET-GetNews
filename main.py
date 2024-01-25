import asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bs4 import BeautifulSoup
import requests
from typing import final
import pymongo
from pymongo import MongoClient
from time import sleep

TOKEN = final("6466778336:AAEobL0_XWIo314UFANHbGL6QaicK8LSEww")
URL = final("https://uet.vnu.edu.vn/category/tin-tuc/tin-sinh-vien/feed/")

client = MongoClient("mongodb+srv://pknstudio2704:nguyenitdev2704@cluster0.xafk9pw.mongodb.net/?retryWrites=true&w=majority")
db = client["UETNews"]
news_collection = db["news"]

def get_news():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "xml")
    item = soup.find("item")
    title = item.find("title").text
    url = item.find("guid").text
    new = {"title": title, "url": url}
    return new


async def create_news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_news()
    check_news = news_collection.find_one(data)
    if check_news:
        await context.bot.send_message(chat_id="@UETNewsNotification", text="exist")
    else:
        result = news_collection.delete_many({})
        news_collection.insert_one(data)
        url = data["url"]
        await update.message.reply_text(f"{url}")


if __name__ == '__main__':
    while True:
        sleep(10)
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("news", create_news))
        app.run_polling()