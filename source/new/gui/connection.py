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
    myResult = mycursor.fetchall()
    if myResult:
        return myResult


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


def button_click(store, gu, dong, addr_frame, map_widget):
    mydb, mycursor = connectDB("project")
    result = executeCommand(
        mydb,
        mycursor,
        "SELECT 상호명,도로명주소 FROM original_shop_seoul WHERE ((상호명 like '%"
        + store
        + "%') and (시군구명 = '"
        + gu
        + "') and (법정동명 ='"
        + dong
        + "')) limit 20",
    )
    string = "Store entered is " + store + " and addr entered is " + gu + " " + dong

    display(addr_frame, map_widget, result, ("Arial", 10))
    print(string)
    return result


def display(addr_frame, map_widget, result, font):
    idx = 0
    addr_frame.grid_columnconfigure(0, weight=1)  # reset grid

    for res in result:
        style = ttk.Style()
        style.configure("res_card.TLabelframe", background="white", padding=5)

        res_card = ttk.LabelFrame(addr_frame, style="res_card.TLabelframe")
        res_card.grid(row=idx, column=0, sticky="we", padx=(0, 10), pady=(0, 5))
        for i in range(len(res)):
            res_label = tk.Label(
                res_card,
                text=res[i],
                font=font,
                background="white",
            )
            res_label.grid(row=i, column=0, sticky="w")
            res_card.bind(
                "<Button-1>",
                lambda event, widget=res_card, addr=res[1]: active(
                    event, widget, addr_frame, addr, map_widget
                ),
            )

        idx += 1

        # Make label text with store title
        # style = ttk.Style()
        # style.configure("res_card.TLabelframe", background="white")

        # res_card = ttk.LabelFrame(frame, text=res[0], style="res_card.TLabelframe")
        # res_card.grid(row=idx, column=0, sticky="we", padx=(0, 10))
        # res_card.bind("<Button-1>", lambda event, widget=res_card: active(event, widget))
        # res_label = tk.Label(
        #     res_card,
        #     text=res[1],
        #     font=font,
        #     background="white",
        # )
        # res_label.grid(row=0, column=0, sticky="w")
        # idx += 1


def active(event, widget, addr_frame, addr, map_widget):
    style = ttk.Style()
    style.configure("on_res_card.TLabelframe", background="lightgrey", padding=5)

    for labelframe in addr_frame.winfo_children():
        labelframe.configure(style="res_card.TLabelframe")
    widget.configure(style="on_res_card.TLabelframe")

    map_widget.set_address(addr, marker=True)


def display_table(frame, title, fields, result, font):
    # Display table title
    title_label = tk.Label(
        frame,
        text=title,
        font=("Arial", 11, "bold"),
        background="azure",
    )
    title_label.grid(row=0, column=1, columnspan=len(result[0]))

    # Q8. Display suitable column names using iteration
    idx = 1
    for field in fields:
        column_label = tk.Label(
            frame, text=field.upper(), background="lightgrey", font=("Arial", 10, "bold")
        )
        column_label.grid(row=1, column=idx)
        frame.grid_columnconfigure(idx, weight=0)  # reset grid
        idx += 1

    idx = 2
    for res in result:
        for col in range(len(res)):
            frame.grid_columnconfigure(idx, weight=0)  # reset grid
            res_label = tk.Label(frame, text=res[col], font=font, background="azure")
            res_label.grid(row=idx, column=col + 1)

        idx += 1

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(len(res) + 1, weight=1)
