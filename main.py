import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")



def start(update, context):
    update.message.reply_text("Hello, How may I help You?")

def helps(update, context):
    update.message.reply_text(
        """
        How are you?
        
        what do you want to do??
        
        /start - to start the bot.
        /contact - how you can contact me.
        /payment - for paying the amount.
        /link - to get the link for details
        /helps - to get help.
        
        
        Come back again...
        """
    )
    
def link(update, context):
    update.message.reply_text("https://falana.in")

def payment(update, context):
    update.message.reply_text("falana_upi@paytm")
    
def contact(update, context):
    update.message.reply_text("Mail at falana@gmail.com")



updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('helps', helps))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatch.add_handler(telegram.ext.CommandHandler('payment', payment))
dispatch.add_handler(telegram.ext.CommandHandler('link', link))


updater.start_polling()
updater.idle()
