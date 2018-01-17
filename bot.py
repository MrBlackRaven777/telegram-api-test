import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import utils
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
# global is_expl_on
# global full_path
# global dirs_list

upd = Updater(token=config.token)
dsp = upd.dispatcher



#def echo(bot, upd):
#    if upd.message.text == "Choose folder":
#        utils.shelve_write(upd.message.chat_id, 'curr_dir', config.start_path)
#        markup = telegram.ReplyKeyboardMarkup(
#            utils.create_markup(utils.explorer(upd.message.chat_id, '')))
#        bot.sendMessage(chat_id=upd.message.chat_id,
#                        text="Select next folder", reply_markup=markup)
#        utils.shelve_write(upd.message.chat_id, 'is_expl_on', True)
#    elif upd.message.text == "Cancel":
#    	utils.shelve_remove(upd.message.chat_id)
#    else:
#        if utils.shelve_read(upd.message.chat_id, 'is_expl_on') == True:
#            curr_dir = utils.shelve_read(upd.message.chat_id, 'curr_dir')
#            new_path = curr_dir + '/' + upd.message.text
#            markup = telegram.ReplyKeyboardMarkup(utils.create_markup(
#                utils.explorer(upd.message.chat_id, upd.message.text)))
#            bot.sendMessage(chat_id=upd.message.chat_id,
#                            text="Select next folder", reply_markup=markup)
#            utils.shelve_write(upd.message.chat_id, 'curr_dir', new_path)
#        else:
#            bot.sendMessage(chat_id=upd.message.chat_id, text="Smth wrong")


    # fav_list = list(config.favorites.keys())
    # markup = telegram.ReplyKeyboardMarkup(utils.create_markup(fav_list))
    # bot.sendMessage(chat_id=upd.message.chat_id,
    #                 text=upd.message.text * 2, reply_markup=markup)

def check_id(bot, upd):
#Check user permission to using bot
    if str(upd.message.chat_id) in config.allowed_id:
        return True        
    else:
        bot.sendMessage(chat_id=upd.message.chat_id,
                    text="You are not allowed to use this bot")
        if config.notify_not_allowed == True:
            bot.sendMessage(chat_id=332761,
                        text="Кто-то стучится в дом, id=" + 
                        str(upd.message.chat_id) + ", зовут " + 
                        upd.message.from_user.first_name + " " +
                        upd.message.from_user.last_name)
        return False
        

def explorer(bot, upd, cpath=""):
    if check_id(bot, upd) == False:
       return
    dirs_list = []
    if config.is_expl_on is True:
        next_dir = upd.message.text
        curr_path = cpath + "/" + next_dir
        utils.shelve_write(upd.message.chat_id, 'curr_path', curr_path)
        os.chdir(curr_path)
        dirs_list = next(os.walk(os.getcwd))[1]
        markup = telegram.ReplyKeyboardMarkup(utils.create_markup(dirs_list,upd.message.chat_id))
        bot.sendMessage(chat_id=upd.message.chat_id, text='Choose next', reply_markup = markup)
    else:
        bot.sendMessage(chat_id=upd.message.chat_id, text='Error')


def path(bot, upd):
    if check_id(bot, upd) == False:
       return
    utils.shelve_create(upd.message.chat_id)
    # utils.shelve_write(upd.message.chat_id, "is_expl_on", True)
    fav_list = list(utils.shelve_read(upd.message.chat_id,'favorites').keys())
    markup = telegram.ReplyKeyboardMarkup(
        utils.create_markup(fav_list, upd.message.chat_id))
    bot.sendMessage(chat_id=upd.message.chat_id,
                    text="Choose folder from favorites, file system or cancel", reply_markup=markup)
    
def echo(bot, upd):
    if check_id(bot, upd) == False:
       return
    favorites = utils.shelve_read(upd.message.chat_id,'favorites')
    fav_list = favorites.keys()
    if upd.message.text in fav_list:
        answer = favorites(upd.message.text)
    markup = telegram.ReplyKeyboardMarkup(
        utils.create_markup(fav_list, upd.message.chat_id))
    bot.sendMessage(chat_id=upd.message.chat_id,
                    text=answer, reply_markup=markup)

def start(bot, upd):
#Starts bot, creates shelves for new user and setting up them with default folders for enviroment, where bot working
    if check_id(bot, upd) == False:
        return
    new_user = True
    for d, dirs, files in os.walk(os.getcwd()):
        for f in files:   
            if str(upd.message.chat_id) in f:
                    new_user = False
    if new_user == True:
        favorites = utils.os_choose()
        curr_dir = favorites.pop("curr_dir")
        utils.shelve_write(upd.message.chat_id, "curr_dir", curr_dir)
        utils.shelve_write(upd.message.chat_id, "favorites", favorites)
        utils.shelve_write(upd.message.chat_id, "is_expl_on", "false")
        reply_text = "Yours OS is: " + os.name + ". Your storage successfully created. Welcome!" 
    else:
        reply_text = "You're already my user. Send me /reset to destroy your personal settings"
    bot.sendMessage(chat_id=upd.message.chat_id, text=reply_text)
    
def reset(bot, upd):
    if check_id(bot, upd) == False:
        return
    markup = telegram.ReplyKeyboardRemove()
    bot.sendMessage(chat_id=upd.message.chat_id, text=utils.shelve_remove(upd.message.chat_id), reply_markup=markup)    
    

def my_id(bot, upd):
#    if check_id(bot, upd) == False:
#        return
    bot.sendMessage(chat_id=upd.message.chat_id, text= "Your id is: " + str(upd.message.chat_id))
    


path_handler = CommandHandler("path", path)
dsp.add_handler(path_handler)

start_handler = CommandHandler("start", start)
dsp.add_handler(start_handler)

reset_handler = CommandHandler("reset", reset)
dsp.add_handler(reset_handler)

echo_handler = MessageHandler(Filters.text, echo)
dsp.add_handler(echo_handler)

expl_handler = CommandHandler("explorer", explorer)
dsp.add_handler(expl_handler)

myid_handler = CommandHandler("myid", my_id)
dsp.add_handler(myid_handler)

upd.start_polling()
upd.idle()
