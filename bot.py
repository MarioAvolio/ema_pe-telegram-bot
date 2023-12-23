from telegram.ext import Updater, MessageHandler, Filters
from telegram import Bot

# Replace 'YOUR_TOKEN' with your bot's API token
TOKEN = 'YOUR_TOKEN'

# Initialize the bot and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the message handler function
def modify_message(update, context):
    # Check if the message is from the specified user in the specified group
    if update.message.chat.username == 'ema_pe':
        modified_text = f"* I AM A CLOWN *\n{update.message.text}\n* I just tell you that I am a clown? *\n* Seriously, I can't stop being a clown! *\n* It's clown o'clock again! *"
        context.bot.send_message(chat_id=update.effective_chat.id, text=modified_text)

# Add the handler to the dispatcher
message_handler = MessageHandler(Filters.text & (~Filters.command), modify_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
