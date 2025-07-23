from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import telegram

# Твой токен
TOKEN = '7418856632:AAFqJZw-kwmU0ZN-ETQK8VTdQem7pL59mc8'

# Канал, на который нужно подписаться
CHANNEL_USERNAME = '@ZetKinoUz'

def start(update: Update, context: CallbackContext):
    user = update.effective_user

    # Кнопки
    buttons = [
        [InlineKeyboardButton("📺 Kanalga o'tish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("✅ Obuna bo'ldim", callback_data='check_sub')]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    update.message.reply_text(
        f"👋 Assalomu alaykum, {user.first_name}!\n\n"
        f"🎥 Kinoni olish uchun avval kanalga obuna bo‘ling!",
        reply_markup=keyboard
    )

def check_subscription(user_id, bot: telegram.Bot):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    bot = context.bot

    if query.data == 'check_sub':
        if check_subscription(user_id, bot):
            bot.send_message(chat_id=user_id, text="✅ Obuna tekshirildi! Endi kodni yuboring.")
        else:
            bot.send_message(chat_id=user_id, text="❌ Iltimos, avval kanalga obuna bo‘ling!")

    query.answer()

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
