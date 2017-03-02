import telegram
from telegram.ext import Updater
import logging
import os
import config

TOKEN=config.token

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(mess age)s', level=logging.INFO)

def start(bot, update): 
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def echo(bot, update):
    texty = update.message.text
    if texty in config.favorites.keys():
        path = config.favorites[texty]
        #os.chdir(path)
        keylist=[]
        #tmplist=[]
        for key in config.favorites.keys():
            tmplist=[]
            tmplist.append(key)
            keylist.append(tmplist)
        
        #keylist = config.favorites.keys()
        #for i in range(ceil(len(keylist)/3))
        #print(keylist)
        keylist.append(["Back","Done","More"])
        mrkup = telegram.ReplyKeyboardMarkup(keylist)                        #[["top left","top right"],["bottom left", "bottom right"]])
        #mrkup = create_markup(config.favorites.keys())
        bot.sendMessage(chat_id=update.message.chat_id, text=os.getcwd(), reply_markup=mrkup) #, one_time_keyboard=True)
    else:
        markup = telegram.ReplyKeyboardRemove()
        bot.sendMessage(chat_id=update.message.chat_id, text="Your id: " + str(update.message.chat_id) + "; you send me: " + update.message.text, reply_markup=markup)

def create_markup(buttons_list):
    #for coll_el in range(lambda n: if n 
    keyboard = list[buttons_tuple]
    markup = telegram.ReplyKeyboardMarkup(keyboard)
    return markup

def cur_dir(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = os.getcwd())

from telegram.ext import CommandHandler, MessageHandler, Filters
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

cur_dir_handler = CommandHandler("cur_dir", cur_dir)
dispatcher.add_handler(cur_dir_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
