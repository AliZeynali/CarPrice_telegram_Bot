import psycopg2,datetime
import sys
# Simple routine to run a query on a database and print the results:
hostname = 'localhost'
username = 'postgres'
password = '137555'
database = 'CarPriceNullatech'


def addElement(Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality, perBrand, perModel):
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    dateAndTime = str(datetime.datetime.now()).split(" ")
    #current date and time will save in dataBase
    date = dateAndTime[0]
    time = dateAndTime[1][0:8]
    sql = "Insert into CarTable (Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality, date, time, perBrand, perModel)" + \
          "\nvalues (\'" + Brand + "\',\'" + Model + "\'," + Price + "," + Drived + "," + MadeYear + ",\'" + FuelType + "\'" + \
          ",\'" + state + "\'" + ",\'" + Color + "\'" + ",\'" + Gear + "\'" + ",\'" + URL + "\'" + ",\'" + nationality +"\'"+ \
          ",\'" + date + "\'" + ",\'" + time + "\'" + ",\'" + perBrand+ "\',"+ "\'" + perModel +  "\')"
    try:
        cur.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError:
        pass


def getBrands():
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    cur.execute("Select Brand, perBrand from CarTable")
    Brands = []
    for brand, perBrand in cur.fetchall():
        if not Brands.__contains__([clearName(str(brand)),clearName(str(perBrand))]):
            Brands.append(clearName([clearName(str(brand)),clearName(str(perBrand))]))
    return Brands


def getModels(brand):
    global hostname, username, password, database
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    sql = "Select Model, perModel from CarTable " + "Where Brand = " + "\'" + brand + "\'"
    cur.execute(sql)
    Models = []
    for model, perModel in cur.fetchall():
        if not Models.__contains__([clearName(str(model)),clearName(str(perModel))]):
            Models.append([clearName(str(model)),clearName(str(perModel))])
    return Models


def clearName(str):
    return str.replace('(', '').replace(')', '').replace(',', '').replace('\'', '')

    # myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    # doQuery( myConnection )
    # myConnection.close()


def temp(conn):
    cur = conn.cursor()
    sql = "select * from CarTable" + " Where Brand Like \'پ%\'"
    cur.execute(sql)
    for Brand, Model, Price, Drived, MadeYear, FuelType, state, Color, Gear, URL, nationality in cur.fetchall():
        print(
            "Brand:  " + Brand + ", Model:  " + str(Model) + ", Drived in Km: " + str(
                Drived) + ", Made Year: " + str(MadeYear) +
            ", Fuel Type: " + FuelType + ", State: " + state + ", Color: " + Color + ", Gear Type: " + Gear + ",  Nationality: " + nationality +
            "\nURL link: " + URL + "\n")
