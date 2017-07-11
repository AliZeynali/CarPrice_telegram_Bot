import psycopg2
import sys
from CarPriceDataBase import *

# Simple routine to run a query on a database and print the results:
hostname = 'localhost'
username = 'postgres'
password = '137555'
database = 'CarPriceNullatech'


def getCurrent(chat_id):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select Count(chat_id) from Users" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    count = cur.fetchall()
    if int(count[0][0]) == 0:
        sql = "insert into Users values ( " + str(chat_id) + " , " + " \'صفحه اصلی\'" + " , null, null, null, null, null )"
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
    sql = "Update Users Set brand = \'" + newModel + "\'" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateYear(chat_id, newYear):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set brand = " + str(newYear) + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def updateDrived(chat_id, newDrived):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update Users Set brand = " + str(newDrived) + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()


def hasBrand(chatID, brand):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select count(brand) from Users Where brand = \'" + brand + "\'"
    count = cur.fetchall()
    answer = False
    if int(count[0]) > 0:
        answer = True
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()
    return answer


def hasModel(chatID, brand, model):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select count(model) from Users Where brand = \'" + brand + "\' and model = \'" + model + "\'"
    count = cur.fetchall()
    answer = False
    if int(count[0]) > 0:
        answer = True
    cur.execute(sql)
    myConnection.commit()
    myConnection.close()
    return answer


def giveData(chatID):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select * from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for chatID, current, brand, model, year, drived, nationality in cur.fetchall():
        Brand = brand
        Model = model
        Year = year
        Drived = drived
        Nationality = nationality
    if year == 1:
        fromYear1 = 1396
        tillYear1 = 1500  # just big number
        fromYear2 = 2017
        tillYear2 = 2100  # just big number
    elif year == 2:
        fromYear1 = 1392
        tillYear1 = 1395
        fromYear2 = 2013
        tillYear2 = 2016
    elif year == 3:
        fromYear1 = 1388
        tillYear1 = 1391
        fromYear2 = 2009
        tillYear2 = 2012
    elif year == 4:
        fromYear1 = 1300
        tillYear1 = 1388
        fromYear2 = 1900
        tillYear2 = 2009

    if Drived == 1:
        leastDrived = 0
        MaxDrived = 2000
    elif Drived == 2:
        leastDrived = 2000
        MaxDrived = 10000
    elif Drived == 3:
        leastDrived = 10000
        MaxDrived = 50000
    elif Drived == 4:
        leastDrived = 50000
        MaxDrived = 80000
    elif Drived == 5:
        leastDrived = 80000
        MaxDrived = 120000
    sql = "Select * from CarTable Where brand = \'" + Brand + "\' and model = \'" + Model + "\' and (year between " + str(
        fromYear1) + \
          " and " + str(tillYear1) + " or year between " + str(fromYear2) + " and " + str(
        tillYear2) + ")  and drived between " + str(leastDrived) + \
          " and " + str(MaxDrived) + " and nationality = \'" + Nationality + "\'"
    if Drived == 6:
        sql = "Select * from CarTable Where brand = \'" + Brand + "\' and model = \'" + Model + "\' and (year between " + str(
            fromYear1) + \
              " and " + str(tillYear1) + " or year between " + str(fromYear2) + " and " + str(
            tillYear2) + ")  and drived >= 120000 " + " and nationality = \'" + Nationality + "\'"
    data = []
    cur.execute(sql)
    for brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality in cur.fetchall():
        data.append({brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality})
    myConnection.close()
    return data


def givePriceSearchData(type):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
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

    sql = "Select * from CarTable Where price  BETWEEN " + str(minPrice) + " and " + str(maxPrice)
    if type == 5:
        sql = "Select * from CarTable Where price > 150000000"

    data = []
    cur.execute(sql)
    for brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality in cur.fetchall():
        data.append({brand, model, price, drived, madeYear, fuelType, state, color, gear, URL, nationality})
    myConnection.close()
    return data


def createBrandsList(chatID):
    string = "برند مورد نظر خود را انتخاب کنید: \n \n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select nationality from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for nationality in cur.fetchall():
        Nationality = nationality
    sql = "Select brand from CarTable Where nationality = \'" + Nationality + "\'"
    cur.execute(sql)
    Brands =[]
    for brand in cur.fetchall():
        if not Brands.__contains__(str(brand)):
            Brands.append(clearName(str(brand)))
    for brand in Brands:
        string += "/" + str(brand) + "\n"
    return string


def createModelsList(chatID):
    string = "مدل خودروی مورد نظر خود را انتخاب کنید: \n \n"
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select nationality, brand from users Where chat_id  = " + str(chatID)
    cur.execute(sql)
    for nationality , brand in cur.fetchall():
        Nationality = nationality
        Brand = brand
    sql = "Select model from CarTable Where nationality = \'" + Nationality + "\' and brand = \'"+ Brand  + "\'"
    cur.execute(sql)
    Models =[]
    for model in cur.fetchall():
        if not Models.__contains__(model):
            Models.append(clearName(str(model)))

    for model in Models:
        string += "/" + str(model) + "\n"
    return string


def tm1():
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Select current from Users" + " Where chat_id = " + str("3")
    cur.execute(sql)
    for x in cur.fetchall():
        print(x[0])

tm1()
