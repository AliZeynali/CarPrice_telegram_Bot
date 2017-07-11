import requests
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from CarPriceDataBase import *
from UsersTable import *

last_update = "notUpdated"
defCurrent = "صفحه اصلی"
markupStart = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="جستجو بر اساس مشخصات")],
                                            [KeyboardButton(text="جستجو بر اساس قیمت")]])
markupBack =  ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="بازگشت به صفحه اصلی")]])
markupPrice = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="زیر 20 میلیون")], [KeyboardButton(text="20 تا 50 میلیون")],
    [KeyboardButton(text="50 تا 100 میلیون")],
    [KeyboardButton(text="100 تا 150 میلیون")], [KeyboardButton(text="بالای 150 میلیون")],
    [KeyboardButton(text="بازگشت به صفحه اصلی")]
])
markupNationality = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ایرانی")], [KeyboardButton(text="خارجی")]])
markupYear = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="جدید تر از 1396 (2017)")], [KeyboardButton(text="از 1392 تا 1395 (2013 - 2016)")],
    [KeyboardButton(text="از 1388 تا 1391 (2009 - 2012)")],
    [KeyboardButton(text="قبل از 1388 (2009)")]
    , [KeyboardButton(text="بازگشت به صفحه اصلی")]
])
markupDrived = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="زیر 2000")], [KeyboardButton(text="2000 تا 10000")],
    [KeyboardButton(text="10000 تا 50000")],
    [KeyboardButton(text="50000 تا 80000")], [KeyboardButton(text="80000 تا 120000")],
    [KeyboardButton(text="بالای 120000")],
    [KeyboardButton(text="بازگشت به صفحه اصلی")]
])

def update_Order(chatID, brand, model, year, drived, nationality):
    # if each of brand,model, year, drived is -1 it wont change
    if brand != -1:
        updateBrnad(chatID, brand)
    if model != -1:
        updateModel(chatID, model)
    if year != -1:
        updateYear(chatID, year)
    if drived != -1:
        updateDrived(chatID, drived)
    if nationality != -1:
        updateNationality(chatID, nationality)


def prettyTime(last_update):
    splited = last_update.split("T")
    date = splited[0]
    time = splited[1]
    months = {'01': 'January', '02': "Febuary", '03': 'March', '04': "April", '05': "May", '06': "June", "07": "July",
              "08": "August",
              '09': "September", '10': "October", '11': "November", '12': "December"}
    date = date.split("-")
    day = date[2]
    year = date[0]
    month = months[date[1]]
    time = time.split(":")
    hour = time[0]
    minutes = time[1]
    str1 = "روز " + str(day) + "\n" + "ماه " + month + "\n" + "سال" + year + " میلادی" + "\n"
    str2 = "ساعت:     " + hour + "   و  " + minutes + "   دقیقه." + "\n"
    return str1 + str2





def nextMarkUp(nextMark, chat_id):
    markup = None
    global markupPrice, markupStart, markupDrived, markupYear, markupNationality, data, Brands, Models
    current = getCurrent(chat_id)

    if nextMark in { "start", "MainMenu", "بازگشت به صفحه اصلی"}:
        markup = markupStart
        setCurrent(chat_id, 'MainMenu')
        update_Order(chat_id, "null", "null", "null", "null", "null")
        return markup, "MainMenu"
    if current in {"start", "MainMenu"}:
        update_Order(chat_id, "null", "null", "null", "null", "null")
        if nextMark == "جستجو بر اساس مشخصات":
            markup = markupNationality
            setCurrent(chat_id, "nationality")
            return markup, "nationality"
        if nextMark == "جستجو بر اساس قیمت":
            markup = markupPrice
            setCurrent(chat_id, "Price")
            return markup, "Price"
    if current == "Price":
        if nextMark in {"زیر 20 میلیون", "20 تا 50 میلیون", "50 تا 100 میلیون",
                        "100 تا 150 میلیون", "بالای 150 میلیون"}:
            markup = markupStart
            setCurrent(chat_id, 'MainMenu')
            return markup, nextMark
    if current == "nationality":
        if nextMark in {"ایرانی", "خارجی"}:
            if nextMark == "ایرانی":
                update_Order(chat_id, -1, -1, -1, -1, "I")
            else:
                updateNationality(chat_id, "F")
                update_Order(chat_id, -1, -1, -1, -1, "F")
            setCurrent(chat_id, "BrandList")
            return markupBack, "BrandList"
    if current == "BrandList":
        if hasBrand(chat_id, nextMark):
            update_Order(chat_id, nextMark, -1, -1, -1, -1)
            setCurrent(chat_id, "ModelList")
            return markupBack, "ModelList"
    if current == "ModelList":
        if hasModel(chat_id, nextMark):
            update_Order(chat_id, -1, nextMark, -1, -1, -1)
            setCurrent(chat_id, "Year")
            markup = markupYear
            return markup, "Year"
    if current == "Year":
        if nextMark in {"جدید تر از 1396 (2017)", "از 1392 تا 1395 (2013 - 2016)", "از 1388 تا 1391 (2009 - 2012)",
                        "قبل از 1388 (2009)"}:
            if nextMark == "جدید تر از 1396 (2017)":
                year = 1
            elif nextMark == "از 1392 تا 1395 (2013 - 2016)":
                year = 2
            elif nextMark == "از 1388 تا 1391 (2009 - 2012)":
                year = 3
            elif nextMark == "قبل از 1388 (2009)":
                year = 4
            update_Order(chat_id, -1, -1, str(year), -1, -1)
            markup = markupDrived
            setCurrent(chat_id, "Drived")
            return markup, "Drived"
    if current == "Drived":
        if nextMark in {"زیر 2000", "2000 تا 10000", "10000 تا 50000", "50000 تا 80000", "80000 تا 120000",
                        "بالای 120000"}:
            markup = markupStart
            if nextMark == "زیر 2000":
                Drived = 1
            elif nextMark == "2000 تا 10000":
                Drived = 2
            elif nextMark == "10000 تا 50000":
                Drived = 3
            elif nextMark == "50000 تا 80000":
                Drived = 4
            elif nextMark == "80000 تا 120000":
                Drived = 5
            elif nextMark == "بالای 120000":
                Drived = 6
            update_Order(chat_id, -1, -1, -1, Drived, -1)
            setCurrent(chat_id, "MainMenu")
            return markup, "Data"
    return None, None  # if unvalid text recieved return None


def on_chat_message(message):
    global current
    content_type, chat_type, chat_id = telepot.glance(message)
    # print(message)
    if content_type == 'text':
        text = message['text']
        text = text.replace("/", "")
        markup, stuff = nextMarkUp(text, chat_id)
        # print(markup)
        # print("text: " + text)
        # print(10 * '*')
        if text == 'start':
            setCurrent(chat_id, "MainMenu")
            markup, stuff = nextMarkUp(text, chat_id)
            bot.sendMessage(chat_id, "سلام!", reply_markup=markup)
        elif markup == None and stuff == None:
            bot.sendMessage(chat_id, "Unvalid!", reply_markup=markup)
        elif markup != None:
            if stuff == "MainMenu":
                bot.sendMessage(chat_id, "لطفا نوع جستجو خود را انتخاب کنید: ", reply_markup=markup)
            if stuff == "Price":
                bot.sendMessage(chat_id, "محدوده قیمت مورد نظر خود را انتخاب کنید: ", reply_markup=markup)
            elif stuff == "nationality":
                bot.sendMessage(chat_id, "خودروی مورد نظرتان  در کدام نوع قرار دارد؟ ",
                                reply_markup=markup)
            elif stuff == "BrandList":
                bot.sendMessage(chat_id, createBrandsList(chat_id), reply_markup=markup )
            elif stuff == "ModelList":
                bot.sendMessage(chat_id, createModelsList(chat_id), reply_markup=markup)
            elif stuff == "Year":
                bot.sendMessage(chat_id, "سال تولید خودروی مدل نظر خود را انتخاب کنید: ", reply_markup=markup)
            elif stuff == "Drived":
                bot.sendMessage(chat_id, "میزان کارکرد خودروی مدل نظر خود را انتخاب کنید: ", reply_markup=markup)
            elif stuff == "Data":
                msg = giveData(chat_id)
                bot.sendMessage(chat_id, msg, reply_markup=markup)
            elif stuff in {"زیر 20 میلیون", "20 تا 50 میلیون", "50 تا 100 میلیون",
                           "100 تا 150 میلیون", "بالای 150 میلیون"}:
                if stuff == "زیر 20 میلیون":
                    type = 1
                elif stuff == "20 تا 50 میلیون":
                    type = 2
                elif stuff == "50 تا 100 میلیون":
                    type = 3
                elif stuff == "100 تا 150 میلیون":
                    type = 4
                elif stuff == "بالای 150 میلیون":
                    type = 5
                msg = givePriceSearchData(type)
                bot.sendMessage(chat_id, msg, reply_markup=markup)


token = "429542432:AAGbrN-i4mQ917LYyLCGXg4eSoqqNiLaATw"
bot = telepot.Bot(token)
bot.message_loop({'chat': on_chat_message})

while True:
    time.sleep(10)
