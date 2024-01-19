from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
import time
def get_news():
    list_news = []

    r = requests.get("https://uet.vnu.edu.vn/category/tin-tuc/tin-sinh-vien/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "post"})

    for new in mydivs:
        # new_dict = {}
        # new_dict["Link: "] = new.a.get("href")
        list_news.append(new.a.get("href"))
    return list_news

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'xin chao {update.effective_user.first_name}')

def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_news()
    update.message.reply_text(f'Tin mới\n {data[0]}')


app = ApplicationBuilder().token("6601081071:AAHviHs7pII7gKCPtbOr-K5sxqoyw1i3ufk").build()

app.add_handler(CommandHandler('true', hello))

app.run_polling()