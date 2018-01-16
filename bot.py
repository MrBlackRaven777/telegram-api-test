import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import utils
import os

# global is_expl_on
# global full_path
# global dirs_list

upd = Updater(token=config.token)
dsp = upd.dispatcher


def echo(bot, upd):
    if upd.message.text == "Choose folder":
        utils.shelve_write(upd.message.chat_id, 'curr_dir', config.start_path)
        markup = telegram.ReplyKeyboardMarkup(
            utils.create_markup(utils.explorer(upd.message.chat_id, '')))
        bot.sendMessage(chat_id=upd.message.chat_id,
                        text="Select next folder", reply_markup=markup)
        utils.shelve_write(upd.message.chat_id, 'is_expl_on', True)
    elif upd.message.text == "Cancel":
    	utils.shelve_remove(upd.message.chat_id)
    else:
        if utils.shelve_read(upd.message.chat_id, 'is_expl_on') == True:
            curr_dir = utils.shelve_read(upd.message.chat_id, 'curr_dir')
            new_path = curr_dir + '/' + upd.message.text
            markup = telegram.ReplyKeyboardMarkup(utils.create_markup(
                utils.explorer(upd.message.chat_id, upd.message.text)))
            bot.sendMessage(chat_id=upd.message.chat_id,
                            text="Select next folder", reply_markup=markup)
            utils.shelve_write(upd.message.chat_id, 'curr_dir', new_path)
        else:
            bot.sendMessage(chat_id=upd.message.chat_id, text="Smth wrong")

    # fav_list = list(config.favorites.keys())
    # markup = telegram.ReplyKeyboardMarkup(utils.create_markup(fav_list))
    # bot.sendMessage(chat_id=upd.message.chat_id,
    #                 text=upd.message.text * 2, reply_markup=markup)


def explorer(bot, upd, cpath=config.start_path):
    dirs_list = []
    if config.is_expl_on is True:
        next_dir = upd.message.text
        config.full_path = cpath + "/" + next_dir
        os.chdir(config.full_path)
        dirs_list = next(os.walk(os.getcwd))[1]
        return dirs_list
    else:
        return "No dirs"


def path(bot, upd):
    utils.shelve_create(upd.message.chat_id)
    # utils.shelve_write(upd.message.chat_id, "is_expl_on", True)
    fav_list = list(config.favorites.keys())
    markup = telegram.ReplyKeyboardMarkup(
        utils.create_markup(fav_list, upd.message.chat_id))
    bot.sendMessage(chat_id=upd.message.chat_id,
                    text="Choose folder from favorites, file system or cancel", reply_markup=markup)


path_handler = CommandHandler("path", path)
dsp.add_handler(path_handler)
echo_handler = MessageHandler(Filters.text, echo)
dsp.add_handler(echo_handler)

upd.start_polling()
