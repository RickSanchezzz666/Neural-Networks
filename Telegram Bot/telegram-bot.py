import telegram
from telegram.ext import Updater, MessageHandler, Filters

def handle_message(update, context):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    response = 'Thanks for your message: ' + text
    context.bot.send_message(chat_id=chat_id, text=response)


bot_token = 'token'
bot = telegram.Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()