import psycopg2
import sys
from CarPriceDataBase import *

# Simple routine to run a query on a database and print the results:
hostname = 'localhost'
username = 'postgres'
password = '137555'
database = 'CarPriceNullatech'

#number of data in each message has been seted equl 10

def getCurrent(chat_id):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select Count(chat_id) from Users" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    count = cur.fetchall()
    if int(count[0][0]) == 0:
        sql = "insert into Users values ( " + str(
            chat_id) + " , " + " \'MainMeu\'" + " , null, null, null, null, null , 0, 0, 0, False)"
        cur.execute(sql)
        myConnection.commit()
        myConnection.close()
        return "صفحه اصلی"
    else:
        sql = "Select current from Users" + " Where chat_id = " + str(chat_id)
        cur.execute(sql)
        current = cur.fetchall()[0][0]
        myConnection.close()
        return current


def updateNationality(chat_id, newNationality):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set nationality = \'" + newNationality + "\'" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def setCurrent(chat_id, newCurrent):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set current = \'" + newCurrent + "\'" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateBrnad(chat_id, newBrand):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set brand = \'" + newBrand + "\'" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateModel(chat_id, newModel):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set model = \'" + newModel + "\'" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateYear(chat_id, newYear):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set year = " + str(newYear) + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateDrived(chat_id, newDrived):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set drived = " + str(newDrived) + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()

def updatePriceSearchtype(chatId, type):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set priceType = " + str(type) + " Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()

def resetListLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set listLevel = 0 Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def resetPriceSearchLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set pricesearchlevel = 0 Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def nextListLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set listLevel = listLevel + 1  Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def lastListLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set listLevel = listLevel - 1  Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def nextPriceSearchLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set pricesearchlevel = pricesearchlevel + 1  Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def lastPriceSearchLevel(chatId):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set pricesearchlevel = pricesearchlevel - 1  Where chat_id = " + str(chatId)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()

def hasNextListLevel(chatID):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select * from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for chatID, current, brand, model, year, drived, nationality, listLevel, pLev, priceType, banned in cur.fetchall():
        Brand = str(brand)
        Model = str(model)
        Year = str(year)
        Drived = str(drived)
        Nationality = str(nationality)
        Level = listLevel
    if Year == "1":
        fromYear1 = 1396
        tillYear1 = 1500  # just big number
        fromYear2 = 2017
        tillYear2 = 2100  # just big number
    elif Year == "2":
        fromYear1 = 1392
        tillYear1 = 1395
        fromYear2 = 2013
        tillYear2 = 2016
    elif Year == "3":
        fromYear1 = 1388
        tillYear1 = 1391
        fromYear2 = 2009
        tillYear2 = 2012
    elif Year == "4":
        fromYear1 = 1300
        tillYear1 = 1388
        fromYear2 = 1900
        tillYear2 = 2009
    elif Year == "5":
        fromYear1 = -1
        tillYear1 = 10000
        fromYear2 = -1
        tillYear2 = 10000

    if Drived == "1":
        leastDrived = 0
        MaxDrived = 2000
    elif Drived == "2":
        leastDrived = 2000
        MaxDrived = 10000
    elif Drived == "3":
        leastDrived = 10000
        MaxDrived = 50000
    elif Drived == "4":
        leastDrived = 50000
        MaxDrived = 80000
    elif Drived == "5":
        leastDrived = 80000
        MaxDrived = 120000
    elif Drived == "7":
        leastDrived = 0
        MaxDrived = 100000000
    if Drived != "6":
        sql = "Select count(*) from CarTable Where brand = \'" + str(Brand) + "\' and model = \'" + str(
            Model) + "\' and (madeyear between " + str(
            fromYear1) + \
              " and " + str(tillYear1) + " or madeyear between " + str(fromYear2) + " and " + str(
            tillYear2) + ")  and drived between " + str(leastDrived) + \
              " and " + str(MaxDrived) + " and nationality = \'" + str(
            Nationality) + "\'"
    elif Drived == "6":
        sql = "Select count(*) from CarTable Where brand = \'" + Brand + "\' and model = \'" + Model + "\' and (madeyear between " + str(
            fromYear1) + \
              " and " + str(tillYear1) + " or madeyear between " + str(fromYear2) + " and " + str(
            tillYear2) + ")  and drived >= 120000 " + " and nationality = \'" + str(
            Nationality) + "\'"
    cur.execute(sql)
    num = cur.fetchall()[0][0]
    myConnection.close()
    # check if there are more items, return yes
    if int(num) > (Level+1)*10:
        return True
    return False

def hasNextPriceLevel(chatID):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select priceSearchLevel, priceType from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for lev , Type in cur.fetchall():
        Level = lev
        type= int(Type)
    if type == 1:
        minPrice = 0
        maxPrice = 20000000
    elif type == 2:
        minPrice = 20000000
        maxPrice = 50000000
    elif type == 3:
        minPrice = 50000000
        maxPrice = 100000000
    elif type == 4:
        minPrice = 100000000
        maxPrice = 150000000

    if type != 5:
        sql = "Select count(*) from CarTable Where price  BETWEEN " + str(minPrice) + " and " + str(
            maxPrice)
    elif type == 5:
        sql = "Select count(*) from CarTable Where price >= 150000000"
    cur.execute(sql)
    num = cur.fetchall()[0][0]
    if int(num)> (Level+1)*10:
        return True
    return False

def hasBrand(chatID, brand):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select count(brand) from CarTable Where brand = \'" + brand + "\'"
    cur.execute(sql)
    count = cur.fetchall()
    answer = False
    if int(count[0][0]) > 0:
        answer = True
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()
    return answer


def hasModel(chatID, model):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "select brand from users where chat_id = " + str(chatID)
    cur.execute(sql)
    for brand in cur.fetchall():
        Brand = brand[0]
    sql = "Select count(model) from CarTable Where brand = \'" + str(Brand) + "\' and model = \'" + model + "\'"
    cur.execute(sql)
    count = cur.fetchall()
    answer = False
    if int(count[0][0]) > 0:
        answer = True
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()
    return answer


def giveData(chatID):
    String = "خودرو هایی با مشخصات مورد نظر شما عبارت اند از:\n\n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select * from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for chatID, current, brand, model, year, drived, nationality, listLevel, pLev, priceType, banned in cur.fetchall():
        Brand = str(brand)
        Model = str(model)
        Year = str(year)
        Drived = str(drived)
        Nationality = str(nationality)
        Level = listLevel
    if Year == "1":
        fromYear1 = 1396
        tillYear1 = 1500  # just big number
        fromYear2 = 2017
        tillYear2 = 2100  # just big number
    elif Year == "2":
        fromYear1 = 1392
        tillYear1 = 1395
        fromYear2 = 2013
        tillYear2 = 2016
    elif Year == "3":
        fromYear1 = 1388
        tillYear1 = 1391
        fromYear2 = 2009
        tillYear2 = 2012
    elif Year == "4":
        fromYear1 = 1300
        tillYear1 = 1388
        fromYear2 = 1900
        tillYear2 = 2009
    elif Year == "5":
        fromYear1 = -1
        tillYear1 = 10000
        fromYear2 = -1
        tillYear2 = 10000

    if Drived == "1":
        leastDrived = 0
        MaxDrived = 2000
    elif Drived == "2":
        leastDrived = 2000
        MaxDrived = 10000
    elif Drived == "3":
        leastDrived = 10000
        MaxDrived = 50000
    elif Drived == "4":
        leastDrived = 50000
        MaxDrived = 80000
    elif Drived == "5":
        leastDrived = 80000
        MaxDrived = 120000
    elif Drived == "7":
        leastDrived = 0
        MaxDrived = 100000000
    if Drived != "6":
        sql = "Select * from CarTable Where brand = \'" + str(Brand) + "\' and model = \'" + str(
            Model) + "\' and (madeyear between " + str(
            fromYear1) + \
              " and " + str(tillYear1) + " or madeyear between " + str(fromYear2) + " and " + str(
            tillYear2) + ")  and drived between " + str(leastDrived) + \
              " and " + str(MaxDrived) + " and nationality = \'" + str(
            Nationality) + "\'" + " order by date desc, time desc"
    elif Drived == "6":
        sql = "Select * from CarTable Where brand = \'" + Brand + "\' and model = \'" + Model + "\' and (madeyear between " + str(
            fromYear1) + \
              " and " + str(tillYear1) + " or madeyear between " + str(fromYear2) + " and " + str(
            tillYear2) + ")  and drived >= 120000 " + " and nationality = \'" + str(
            Nationality) + "\'" + " order by date desc, time desc"
    data = []
    cur.execute(sql)

    for brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality, date, time, perBrand, perModel in cur.fetchall():
        data.append([perBrand, perModel, price, drived, madeYear, fuelType, state, color, gear, URL, nationality])
    myConnection.close()

    #   Send message size is limited (about 4000 characters.) so we only send last 10 items.
    #   elementInPage shows how many element will show in each message

    elementInPage = 10
    minIndex = Level * elementInPage
    maxIndex = min((Level + 1) * elementInPage - 1, len(data) - 1)
    for car in data[minIndex:maxIndex+1]:
        if car[2] == -1:
            car[2] = "تماس بگیرید"
        String += "برند:   " + str(car[0]) + "\n" + "مدل:   " + str(car[1]) + "\n" + "سال تولید:   " + str(
            car[4]) + "\n" + "قیمت:   " + str(car[2]) + "   تومان\n" + "کارکرد:   " + str(car[3]) + "   کیلومتر\n" + "نوع سوخت مصرفی:   " + str(
            car[5]) + "\n" + "رنگ:   " + str(
            car[7]) + "\n" + "نوع گیربکس:   " + str(car[8]) + "\n" + "استان:   " + str(car[6]) + "\n" + str(
            car[9]) + "\n" + 30 * "-" + "\n"
    if String == "خودرو هایی با مشخصات مورد نظر شما عبارت اند از:\n\n":
        return "خودرویی با مشخصات مورد نظر شما یافت نشد!" + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
               "Nullatech.com"
    return String + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
           "Nullatech.com"


def givePriceSearchData(chatID):
    String = "خودروهای در محدوده قیمت مورد نظر شما عبارت اند از:\n\n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select priceSearchLevel , priceType from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for lev , Type in cur.fetchall():
        Level = lev
        type = int(Type)
    if type == 1:
        minPrice = 0
        maxPrice = 20000000
    elif type == 2:
        minPrice = 20000000
        maxPrice = 50000000
    elif type == 3:
        minPrice = 50000000
        maxPrice = 100000000
    elif type == 4:
        minPrice = 100000000
        maxPrice = 150000000

    if type != 5:
        sql = "Select * from CarTable Where price  BETWEEN " + str(minPrice) + " and " + str(
            maxPrice) + " order by date desc, time desc"
    elif type == 5:
        sql = "Select * from CarTable Where price >= 150000000" + " order by date desc, time desc"

    data = []
    cur.execute(sql)
    for brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality, date, time, perBrand, perModel in cur.fetchall():
        data.append([perBrand, perModel, price, drived, madeYear, fuelType, state, color, gear, URL, nationality])
    myConnection.close()

    #   Send message size is limited (about 4000 characters.) so we only send last 10 items.
    elementInPage = 10
    minIndex = Level * elementInPage
    maxIndex = min((Level + 1) * elementInPage - 1, len(data) - 1)
    for car in data[minIndex:maxIndex+1]:
        String += "برند:   " + str(car[0]) + "\n" + "مدل:   " + str(car[1]) + "\n" + "سال تولید:   " + str(
            car[4]) + "\n" + "قیمت:   " + str(car[2]) + "\n" + "کارکرد:   " + str(car[3]) + "\n" + "نوع سوخت مصرفی:   " + str(
            car[5]) + "\n" + "رنگ:   " + str(
            car[7]) + "\n" + "نوع گیربکس:   " + str(car[8]) + "\n" + "استان:   " + str(car[6]) + "\n" + str(
            car[9]) + "\n" + 30 * "-" + "\n"
    if String == "خودروهای در محدوده قیمت مورد نظر شما عبارت اند از:\n\n":
        return "خودرویی در محدوده قیمتی مورد نظر شما یافت نشد!" + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
               "Nullatech.com"
    return String + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
           "Nullatech.com"

def createBrandsList(chatID):
    string = "برند مورد نظر خود را انتخاب کنید: \n \n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select nationality from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for nationality in cur.fetchall():
        Nationality = nationality[0]
    sql = "Select brand , perBrand from CarTable Where nationality = \'" + str(Nationality) + "\'"
    cur.execute(sql)
    Brands = []
    for brand , perBrand in cur.fetchall():
        if not Brands.__contains__([clearName(str(brand)),clearName(str(perBrand))]):
            Brands.append([clearName(str(brand)),clearName(str(perBrand))])
    for brand in Brands:
        string +=  "/" + str(brand[0]) + "        " +str(brand[1]).replace("_"," ")+ "\n\n"
    if string == "برند مورد نظر خود را انتخاب کنید: \n \n":
        return "برندی یافت نشد!" + "\n\n" + "بازگشت به صفحه اصلی:   " + "/MainMenu" + "\n\n" + \
               "Nullatech.com"
    return string + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
           "Nullatech.com"


def createModelsList(chatID):
    string = "مدل خودروی مورد نظر خود را انتخاب کنید: \n \n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select nationality, brand from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for nationality, brand in cur.fetchall():
        Nationality = nationality
        Brand = brand
    sql = "Select model , perModel from CarTable Where nationality = \'" + Nationality + "\' and brand = \'" + Brand + "\'"
    cur.execute(sql)
    Models = []
    for model, perModel in cur.fetchall():
        if not Models.__contains__([clearName(str(model)), clearName(str(perModel))]):
            Models.append([clearName(str(model)), clearName(str(perModel))])

    for model in Models:
        string += "/" +str(model[0])  +  "        "+ str(model[1]).replace("_"," ")+ "\n\n"
    if string == "مدل خودروی مورد نظر خود را انتخاب کنید: \n \n":
        return "مدلی با این نام برند، یافت نشد!" + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
               "Nullatech.com"
    return string + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
           "Nullatech.com"


def tm1():
    string = "مدل خودروی مورد نظر خود را انتخاب کنید: \n \n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    # sql = "Select nationality, brand from users Where chat_id  = " + str(chatID)
    # cur.execute(sql)
    # for nationality, brand in cur.fetchall():
    #     Nationality = nationality
    #     Brand = brand
    Nationality = "I"
    Brand = "Peugeout"
    sql = "Select model from CarTable Where nationality = \'" + Nationality + "\' and brand = \'" + Brand + "\'"
    cur.execute(sql)
    Models = []
    for model in cur.fetchall():
        if not Models.__contains__(clearName(str(model))):
            Models.append(clearName(str(model)))

    for model in Models:
        string += "/" + str(model) + "\n"
    if string == "مدل خودروی مورد نظر خود را انتخاب کنید: \n \n":
        return "مدلی با این نام برند، یافت نشد!" + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
               "Nullatech.com"
    return string + "\n\n" + "بازگشت به صفحه اصلی: " + "/MainMenu" + "\n\n" + \
           "Nullatech.com"

