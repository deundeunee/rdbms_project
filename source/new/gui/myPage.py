import tkinter as tk
from tkinter import ttk, messagebox
from connection import *


def news(middle_frame, parent):

    db, c = connectDB("project")

    # clear all widget
    for widget in middle_frame.winfo_children():
        widget.destroy()
    middle_frame.pack_forget()

    # activate query
    c.execute("select * from my_news where user_id = '" + parent.user_id + "'")
    result = c.fetchall()
    # Label in top row
    label2 = tk.Label(middle_frame, text=parent.user_id + "'s PAGE", bg="white", font=("Arial", 14))
    label2.grid(row=0, column=0, columnspan=4)

    # Print table columns, starting from row 1
    columns = c.column_names
    k = 0
    i = 2
    for cols in columns:
        res_label = tk.Label(middle_frame, text=cols)
        res_label.grid(row=1, column=k)
        # start from row=1, col=0
        k = k + 1
    for res in result:
        middle_frame.rowconfigure(i, weight=0)
        for j in range(len(res)):
            # print(res[j])
            res_label = tk.Label(middle_frame, text=res[j], bg="white")
            res_label.grid(row=i, column=j)
        i = i + 1
    middle_frame.rowconfigure(len(result) + 2, weight=1)


def place(middle_frame, parent):
    def showInput(event, entry, data, label):
        print(data)
        query = """update my_place set memo=%s where ((my_place_id=%s) and (user_id=%s))"""
        memo = entry.get()
        c.execute(query, (memo, data[0], parent.user_id))
        db.commit()
        label.config(text=memo)
        # entry.delete(0, END)
        messagebox.showinfo("Success", "This memo is added in your page")

    db, c = connectDB("project")

    # clear all widget
    for widget in middle_frame.winfo_children():
        widget.destroy()

    # activate query
    c.execute(
        "select p. my_place_id, o.상호명, p.memo from my_place p join original_shop_seoul o on p.shop_id=o.상가업소번호 where user_id = '"
        + parent.user_id
        + "'"
    )
    result = c.fetchall()
    # Label in top row
    label2 = tk.Label(middle_frame, text=parent.user_id + "'s PAGE", bg="white", font=("Arial", 14))
    label2.grid(row=0, column=0, columnspan=4)
    # Print table columns, starting from row 1
    columns = c.column_names
    k = 0
    i = 2
    for cols in columns:
        col_label = tk.Label(middle_frame, text=cols)
        col_label.grid(row=1, column=k)
        # start from row=1, col=0
        k = k + 1
    for res in result:
        middle_frame.rowconfigure(i, weight=0)
        for j in range(len(res)):
            # print(res[j])
            res_label = tk.Label(middle_frame, text=res[j], bg="white")
            res_label.grid(row=i, column=j)
        entry = tk.Entry(middle_frame)
        entry.grid(row=i, column=len(res))
        entry.bind(
            "<Return>",
            lambda event, data=res, entry=entry, label=res_label: showInput(
                event, entry, data, label
            ),
        )
        i = i + 1
    middle_frame.rowconfigure(i, weight=1)


class My_page(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        db, c = connectDB("project")
        c.execute(
            "CREATE TABLE if not exists my_place(my_place_id INT AUTO_INCREMENT PRIMARY KEY, user_id  VARCHAR(255), shop_id INT, memo VARCHAR(255))"
        )
        db.commit()
        c.execute(
            "CREATE TABLE if not exists my_news(news_id INT AUTO_INCREMENT PRIMARY KEY, user_id  VARCHAR(255), news_title VARCHAR(255), url VARCHAR(255))"
        )
        db.commit()

        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame
        top_frame = parent.get_frame("main").top_frame

        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=1)
        middle_frame.columnconfigure(2, weight=1)
        middle_frame.columnconfigure(3, weight=1)

        # Label in top row
        label2 = tk.Label(
            middle_frame, text=parent.user_id + "'s PAGE", bg="white", font=("Arial", 14)
        )
        label2.grid(row=0, column=0, columnspan=4)

        button1 = tk.Button(top_frame, text="News", command=lambda: news(middle_frame, parent))
        button1.pack(side="right", padx=10)
        button2 = tk.Button(top_frame, text="Place", command=lambda: place(middle_frame, parent))
        button2.pack(side="right", padx=5)

        place(middle_frame, parent)
