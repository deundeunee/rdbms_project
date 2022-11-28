import mysql.connector
import tkinter as tk
from tkinter import ttk


def connectDB(db_use):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="skku", database=db_use)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use " + db_use)

    return mydb, mycursor
    # Connected to the database
    # Now we can create instances of DB connection and cursor, ex) mydb, mycursor = connectDB("test")


# Execute the sql command
def executeCommand(mydb, mycursor, command):
    try:
        mycursor.execute(command)
        mydb.commit()
    except:
        # Rollback in case there is any error
        mydb.rollback()

    try:
        myResult = mycursor.fetchall()
        return myResult
    except:
        print("result fetch error")


# Build an sql query
def build_sql_query(fields, table, conditions=None):
    fields = ",".join(fields)
    if conditions:
        return "SELECT " + fields + " FROM " + table + " WHERE " + conditions + " LIMIT 15"
    else:
        return "SELECT " + fields + " FROM " + table + " LIMIT 15"


def printAll(mycursor, tbl):
    mycursor.execute("SELECT * from " + tbl)
    myResult = mycursor.fetchall()
    for row in myResult:
        print(row)
    # printAll("original_shop_seoul", "project") prints all the rows in 'original_shop_seoul.csv'


def printHead(mycursor, tbl):
    mycursor.execute("SELECT * from " + tbl + " limit 10")
    myResult = mycursor.fetchall()
    for row in myResult:
        print(row)
    # printHead("original_shop_seoul", "project") prints only first 10 rows in 'original_shop_seoul.csv'
