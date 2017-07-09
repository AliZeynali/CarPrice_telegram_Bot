import psycopg2
import sys

# Simple routine to run a query on a database and print the results:
hostname = 'localhost'
username = 'postgres'
password = '137555'
database = 'CarPriceNullatech'


def printAllValues():
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()

    cur.execute("SELECT * FROM CarTable")

    for Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL , nationality in cur.fetchall():
        print(
            "Brand:  " + Brand.replace(' ', '') + ", Model:  " + str(Model).replace(' ', '') + ", Drived in Km: " + str(
                Drived) + ", Made Year: " + str(MadeYear) +
            ", Fuel Type: " + FuelType.replace(' ', '') + ", State: " + state.replace(' ',
                                                                                      '') + ", Color: " + Color.replace(
                ' ', '') + ", Gear Type: " + Gear.replace(' ', '') + ",  Nationality: "+ nationality +
             "\nURL link: " + URL+"\n")


def addElement(Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality):
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    sql = "Insert into CarTable (Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality)"+\
          "\nvalues (\'" + Brand + "\',\'"+Model + "\',"+ Price +"," + Drived+ "," + MadeYear + ",\'"+FuelType + "\'"+\
          ",\'" + state + "\'" + ",\'"+Color + "\'" + ",\'"+Gear + "\'" + ",\'" +URL + "\'" + ",\'" + nationality + "\')"
    cur.execute(sql)
    conn.commit()

def getBrands():
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    cur.execute("Select Brand from CarTable")
    Brands = []
    for brand in cur.fetchall():
        if not Brands.__contains__(clearName(str(brand))):
            Brands.append(clearName(str(brand)))
    return Brands


def getModels(brand):
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    sql = "Select Model from CarTable " + "Where Brand = " +"\'" +  brand + "\'"
    cur.execute(sql)
    Models =[]
    for model in cur.fetchall():
        if not Models.__contains__(model):
            Models.append(clearName(str(model)))
    return Models

def searchByPrice(minPrice, maxPrice):
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    #if maxPrice is -1, it means that maxPrice doesn't matter.
    cur = conn.cursor()
    if maxPrice != -1:
        sql = "Select * from CarTable "+ "Where Price between "+ minPrice +" AND " +  maxPrice
    else:
        sql = "Select * from CarTable " + "Where Price >= " +  minPrice
    cur.execute(sql)
    data = []
    for Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality in cur.fetchall():
        data.append([Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality])
    return data



def clearName(str):
    return str.replace('(', '').replace(')', '').replace(',', '').replace('\'', '')

    # myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    # doQuery( myConnection )
    # myConnection.close()

def temp(conn):
    cur = conn.cursor()
    sql = "select * from CarTable" +" Where Brand Like \'پ%\'"
    cur.execute(sql)
    for Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL , nationality in cur.fetchall():
        print(
            "Brand:  " + Brand+ ", Model:  " + str(Model) + ", Drived in Km: " + str(
                Drived) + ", Made Year: " + str(MadeYear) +
            ", Fuel Type: " + FuelType + ", State: " + state + ", Color: " + Color + ", Gear Type: " + Gear + ",  Nationality: "+ nationality +
             "\nURL link: " + URL+"\n")
