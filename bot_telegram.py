#$ pip install pyTelegramBotAPI

import telebot
import random
from telebot import types





my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton("back")
key2 = types.KeyboardButton("forward")
key3 = types.KeyboardButton("test1")
key4 = types.KeyboardButton("test2")
key5 = types.KeyboardButton("test3")
key6 = types.KeyboardButton("test4")
my_keyboard.add(key1,key2,key3,key4,key5,key6)





bot = telebot.TeleBot("your key", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
 
'''''
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "پیام تستی")
'''''  

'''''
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	 bot.send_message(message.chat.id, "پیام تستی")
''''' 
 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "سلام":
	    bot.send_message(message.chat.id, "علیک سلام")
    
    elif message.text == "خوبی":
        bot.send_message(message.chat.id, "ممنون")
    elif message.text == "عکس قدی بده":
        photo = open("C:/Users/Farhad/Pictures/wallpaper/1312721.jpeg" , "rb")
        bot.send_message(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "نمیفهمم چی میگی", reply_markup= my_keyboard)
        
        
@bot.message_handler(commands=["fal"])
def send_fal(message):
    fal_list = ["hi there","idbvjvb","dysydgfks"]
    selected_fal = random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)
           

 
bot.infinity_polling()
 
