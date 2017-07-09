import psycopg2
import sys

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
    if int(count[0]) == 0:
        sql = "insert into Users values ( " + chat_id + " , " + " \'صفحه اصلی\'" + " )"
        cur.execute(sql)
        myConnection.commit()
        return "صفحه اصلی"
    else:
        sql = "Select current from Users" + " Where chat_id = " + str(chat_id)
        return cur.fetchall()[0][0]

def setCurrent(chat_it , newCurrent):
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    sql = "Update table Users Set current = \'" + newCurrent +"\'" " Where chat_id = "+ str(chat_it)

def tm1 ():
    global hostname, username, password, database
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    chat_id = 1
    sql = "Select Count(chat_id) from Users" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    for x in cur.fetchall():
        print("X is: " + str(x[0]))
        count = x
        print(count[0])
    sql = "Select current from Users" + " Where chat_id = " + str(chat_id)
    cur.execute(sql)
    x = cur.fetchall()[0][0]
    current = x
    print(current)

