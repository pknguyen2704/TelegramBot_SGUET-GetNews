from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, filters, Updater

# Thay thế 'YOUR_BOT_TOKEN' bằng mã token của bot bạn đã tạo trên BotFather
BOT_TOKEN = '6466778336:AAEobL0_XWIo314UFANHbGL6QaicK8LSEww'

# Thay thế 'YOUR_CHAT_ID' bằng ID của nhóm bạn muốn gửi tin nhắn
GROUP_CHAT_ID = '-4118192575'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot đã khởi động!')

def send_message(update: Update, context: CallbackContext) -> None:
    # Lấy nội dung tin nhắn từ người dùng
    message_text = update.message.text

    # Gửi tin nhắn vào nhóm
    context.bot.send_message(chat_id=GROUP_CHAT_ID, text=message_text)

def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    # Đăng ký các lệnh xử lý
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Đăng ký lệnh xử lý để gửi tin nhắn từ người dùng đến nhóm
    message_handler = MessageHandler(filters.text & ~filters.command, send_message)
    dispatcher.add_handler(message_handler)

    # Bắt đầu lắng nghe các sự kiện
    updater.start_polling()

    # Dừng chương trình khi nhận được tín hiệu Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
