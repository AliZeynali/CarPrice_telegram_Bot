import requests
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

last_update = "notUpdated"
defCurrent = "صفحه اصلی"
current = {}
data ={}
Brands = {}
Models = {}
markupStart = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="جستجو بر اساس مشخصات")],
                                            [KeyboardButton(text="جستجو بر اساس قیمت")]])
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


def update_data():
    global last_update
    url = "http://138.201.72.172:8000/api/V1"
    response = requests.get(url).json()
    last_update = response['updated']

def update_Brands(chatID, typeNumber):
    pass #TODO
def update_Models(chatID, brandName):
    pass #TODO
def update_Order(chatID, order):
    global data, Brands, Models
    if order == "reset":
        data[chatID] =[]
        Brands[chatID]=[]
        Models[chatID] = []
    data[chatID].append(order)
    return

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
def createBrandsList(chatID):
    string = ""
    #TODO Create text for send Brands List
    return string
def createModelsList(chatID):
    string = ""
    #TODO Create text for send Models List
    return string


def nextMarkUp(nextMark, chat_id):
    markup = None
    global current, markupPrice, markupStart, markupDrived, markupYear, markupNationality, data, Brands, Models
    current1 = getCurrent(chat_id)

    if nextMark in {"/start" , "/MainMenu", "بازگشت به صفحه اصلی"}:
        markup = markupStart
        setCurrent(chat_id) = "صفحه اصلی"
        update_Order(chat_id, "reset")
        return markup, None
    if current1 in {"/start", "صفحه اصلی"}:
        update_Order(chat_id, "reset")
        if nextMark == "جستجو بر اساس مشخصات":
            markup = markupBrandChar
            setCurrent(chat_id) = "BrandChar"
            return markup, "BrandChar"
        if nextMark == "جستجو بر اساس قیمت":
            markup = markupPrice
            setCurrent(chat_id) = "قیمت"
            return markup, "قیمت"
    if current1 == "قیمت":
        if nextMark in {"زیر 20 میلیون","20 تا 50 میلیون", "50 تا 100 میلیون",
                        "100 تا 150 میلیون","بالای 150 میلیون"}:
            markup = markupStart
            setCurrent(chat_id) = "صفحه اصلی"
            return markup, nextMark
        elif nextMark == "بازگشت به صفحه اصلی":
            markup = markupStart
            setCurrent(chat_id) = "صفحه اصلی"
            update_Order(chat_id, "reset")
            return markup, None
    if current1 == "nationality":
        if nextMark in {"از الف تا ب" , "از پ تا خ", "از د تا س", "از ش تا گ",
                        "از ل تا ی"}:
            update_Brands(chat_id, nextMark)
            markup = markupBrandKeyboard
            setCurrent(chat_id) = "BrandList"
            return markup, "BrandList"
        elif nextMark == "بازگشت به صفحه اصلی":
            markup = markupStart
            setCurrent(chat_id) = "صفحه اصلی"
            update_Order(chat_id, "reset")
            return markup, None
    if current1 == "BrandList":
        if nextMark in Brands[chat_id]:
            update_Order(chat_id, nextMark)
            update_Models(chat_id, nextMark)
            markup = markupModelKeyboard
            setCurrent(chat_id) = "ModelList"
            return markup, "ModelList"
        elif nextMark == "بازگشت به صفحه اصلی":
            markup = markupStart
            update_Order(chat_id, "reset")
            setCurrent(chat_id) = "صفحه اصلی"
            return markup, None
    if current1 == "ModelList":
        if nextMark in Models[chat_id]:
            update_Order(chat_id,nextMark)
            setCurrent(chat_id) = "Year"
            markup = markupYear
            return markup, "Year"
        elif nextMark == "بازگشت به صفحه اصلی":
            setCurrent(chat_id) = "صفحه اصلی"
            markup = markupStart
            update_Order(chat_id, "reset")
            return markup, None
    if current1 == "Year":
        if nextMark in {"جدید تر از 1396 (2017)", "از 1392 تا 1395 (2013 - 2016)", "از 1388 تا 1391 (2009 - 2012)",
                        "قبل از 1388 (2009)"}:
            update_Order(chat_id, nextMark)
            markup = markupDrived
            setCurrent(chat_id) = "Drived"
            return markup, "Drived"
        elif nextMark == "بازگشت به صفحه اصلی":
            markup = markupStart
            setCurrent(chat_id) = "صفحه اصلی"
            update_Order(chat_id,nextMark)
            return markup, None
    if current1 == "Drived":
        if nextMark in {"زیر 2000", "2000 تا 10000", "10000 تا 50000", "50000 تا 80000", "80000 تا 120000",
                        "بالای 120000"}:
            markup = markupStart
            update_Order(chat_id, nextMark)
            setCurrent(chat_id) = "صفحه اصلی"
            return markup, "Data"
        elif nextMark == "بازگشت به صفحه اصلی":
            markup = markupStart
            setCurrent(chat_id) = "صفحه اصلی"
            update_Order(chat_id,"reset")
            return markup, None

    return None, None  # if unvalid text recieved return None


def reset_current(chat_id):
    global current
    try:
        current[chat_id] = "صفحه اصلی"
    except KeyError:
        current.update({chat_id: "صفحه اصلی"})


def on_chat_message(message):
    global current
    content_type, chat_type, chat_id = telepot.glance(message)
    print(message)
    if content_type == 'text':
        text = message['text']
        markup, stuff = nextMarkUp(text, chat_id)
        print(markup)
        print("text: " + text)
        print(10 * '*')
        if text == '/start':
            reset_current(chat_id)
            markup, stuff = nextMarkUp(text, chat_id)
            bot.sendMessage(chat_id, "سلام!", reply_markup=markup)
        elif markup == None:
            bot.sendMessage(chat_id, "Unvalid!", reply_markup=markup)
        elif markup != None:
            if stuff == None:
                bot.sendMessage(chat_id, "انتخاب کنید: ", reply_markup=markup)
            else:
                if stuff == "قیمت":
                    bot.sendMessage(chat_id, "محدوده قیمت مورد نظر خود را انتخاب کنید: ", reply_markup=markup)
                elif stuff == "nationality":
                    bot.sendMessage(chat_id, "کشور تولید کننده خودروی مورد نظرتان را انتخاب کنید: ", reply_markup=markup)
                elif stuff == "BrandList":
                    bot.sendMessage(chat_id, createBrandsList(chat_id))
                elif stuff == "Models":
                    bot.sendMessage(chat_id, createModelsList(chat_id))
                elif stuff == "Year":
                    bot.sendMessage(chat_id, "سال تولید خودروی مدل نظر خود را انتخاب کنید: ", reply_markup=markup)
                elif stuff == "Drived":
                    bot.sendMessage(chat_id, "میزان کارکرد خودروی مدل نظر خود را انتخاب کنید: ", reply_markup=markup)
                elif stuff == "Data":
                    #TODO How to manage giving data information
                    update_data()
                    msg = "تاریخ به روز رسانی: " + "\n" + prettyTime(last_update) + "\n" + "\n" + 35 * '-' + "\n" + str(
                        "THIS IS DATA" + "\n" + "nullatech.com")
                    bot.sendMessage(chat_id, msg, reply_markup=markup)
                elif stuff in {"زیر 20 میلیون","20 تا 50 میلیون", "50 تا 100 میلیون",
                        "100 تا 150 میلیون","بالای 150 میلیون"}:
                    #TODO Handle giving price data
                    msg =" "
                    bot.sendMessage(chat_id, msg, reply_markup= markup)



token = "429542432:AAGbrN-i4mQ917LYyLCGXg4eSoqqNiLaATw"
bot = telepot.Bot(token)
bot.message_loop({'chat': on_chat_message})

while True:
    time.sleep(10)
