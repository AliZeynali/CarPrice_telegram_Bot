import requests
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from CarPriceDataBase import *
from UsersTable import *

token = "429542432:AAGbrN-i4mQ917LYyLCGXg4eSoqqNiLaATw"
bot = telepot.Bot(token)
bot.sendMessage(63961974, 4050*'*')