import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")



def start(update, context):
    update.message.reply_text("Ram Ram Bhai")

def helps(update, context):
    update.message.reply_text(
        """
        Ram Ram Bhai,
        
        Aap ko kya krna hai??
        
        /start - to start baat-cheet
        /contact - aap mujhe main kr skte h
        /helps - to get madad        
        Bhagwan aapka bhala kre...
        """
    )
    
def contact(update, context):
    update.message.reply_text("Ram Ram Bhai, Mail at Totatoatota")



updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('helps', helps))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))



updater.start_polling()
updater.idle()
