import telebot
from telebot import types

# @megabotyara_bot
token = "5942438999:AAGR1n7TUDC8iG2wM0lMh6ej1CJ8TsShmfQ"
bot = telebot.TeleBot(token)

newWorker = types.InlineKeyboardButton(text="Новый работник",callback_data="new_worker")
newTeam = types.InlineKeyboardButton(text="Новая команда",callback_data="new_team")
default = types.InlineKeyboardMarkup().add(newWorker).add(newTeam)

@bot.message_handler(content_types=['text'])
def any_other(message):
    bot.send_message(message.from_user.id, message.text, reply_markup=default)
    bot.delete_message(message.chat.id, message.message_id)
    print(message)


@bot.callback_query_handler(func=lambda x: True)
def ananas(call):
    bot.send_message(call.from_user.id, call.data, reply_markup=default)
    try:
        bot.delete_message(call.from_user.id, call.message.message_id)
    except:
        True
    print(call)

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    bot.send_message(message.id)

bot.polling()
