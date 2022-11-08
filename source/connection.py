import mysql.connector

def connectDB(db_use):
    mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd = "skku",
        database = db_use
        )
    mycursor = mydb.cursor(buffered = True)

    return mydb, mycursor
    # Connected to the database
    # Now we can create instances of DB connection and cursor, ex) mydb, mycursor = connectDB("test")

def printAll(tbl, db_use):
    mycursor.execute("SELECT * from "+tbl)
    myResult = mycursor.fetchall()
    for row in myResult:
        print(row)
    # printAll("original_shop_seoul", "project") prints all the rows in 'original_shop_seoul.csv'

def printHead(tbl):
    mycursor.execute("SELECT * from "+tbl+" limit 10")
    myResult = mycursor.fetchall()
    for row in myResult:
        print(row)
    # printHead("original_shop_seoul", "project") prints only first 10 rows in 'original_shop_seoul.csv'

def printCommand(command):
    try: 
        mycursor.execute(command)
        mydb.commit()
    except:
        # Rollback in case there is any error
        mydb.rollback()
    myResult = mycursor.fetchall()
    print("\nRESULT of", command)
    for row in myResult:
        print(row)
    return myResult
    # prints the result of the command

mydb, mycursor = connectDB("project")
mycursor.execute("use project")
# printHead("original_shop_seoul")

command1 = "SELECT 상호명,도로명주소 FROM original_shop_seoul WHERE ((상호명 like '%파리바게뜨%') and (시군구명 = '종로구')) limit 20"
# printCommand(command1)