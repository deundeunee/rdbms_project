import tkinter as tk
from tkinter import ttk, messagebox
from connection import *

db, c = connectDB("project")


def news(middle_frame):
    # clear all widget
    for widget in middle_frame.winfo_children():
        widget.destroy()
    middle_frame.pack_forget()

    # activate query
    c.execute(
        """
                                select * from my_news """
    )  # user_id로 필터링 되는 코드 추가하기
    result = c.fetchall()
    # Label in top row
    label2 = tk.Label(middle_frame, text="YOUR PAGE", bg="white", font=("Arial", 14))
    label2.grid(row=0, column=1, columnspan=2)

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
        for j in range(len(res)):
            # print(res[j])
            res_label = tk.Label(middle_frame, text=res[j], bg="white")
            res_label.grid(row=i, column=j)
        i = i + 1


def place(middle_frame):
    # clear all widget
    for widget in middle_frame.winfo_children():
        widget.destroy()
    middle_frame.pack_forget()

    # activate query
    c.execute(
        """
                                select * from my_place """
    )  # user_id로 필터링 되는 코드 추가하기
    result = c.fetchall()
    # Label in top row
    label2 = tk.Label(middle_frame, text="YOUR PAGE", bg="white", font=("Arial", 14))
    label2.grid(row=0, column=1, columnspan=2)

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
        for j in range(len(res)):
            # print(res[j])
            res_label = tk.Label(middle_frame, text=res[j], bg="white")
            res_label.grid(row=i, column=j)
        entry = tk.Entry(middle_frame)
        entry.grid(row=i, column=len(res))
        i = i + 1


class My_page(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame
        top_frame = parent.get_frame("main").top_frame

        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=1)
        middle_frame.columnconfigure(2, weight=1)
        middle_frame.columnconfigure(3, weight=1)
        middle_frame.columnconfigure(4, weight=1)
        c.execute(
            """
                        select * from my_place """
        )  # user_id로 필터링 되는 코드 추가하기
        result = c.fetchall()
        # Label in top row
        label2 = tk.Label(middle_frame, text="YOUR PAGE", bg="white", font=("Arial", 14))
        label2.grid(row=0, column=1, columnspan=2)

        button1 = tk.Button(top_frame, text="News", command=lambda: news(middle_frame))
        button1.pack(side="right", padx=10)
        button2 = tk.Button(top_frame, text="Place", command=lambda: place(middle_frame))
        button2.pack(side="right", padx=5)
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
            for j in range(len(res)):
                # print(res[j])
                res_label = tk.Label(middle_frame, text=res[j], bg="white")
                res_label.grid(row=i, column=j)
            entry = tk.Entry(middle_frame)
            entry.grid(row=i, column=len(res))

            def showInput(event):
                query = """update my_place set memo=%s where shop_id=%s """
                memo = entry.get()
                c.execute(query, (memo, res[1]))
                db.commit()
                res_label.config(text=memo)
                # entry.delete(0, END)
                messagebox.showinfo("Success", "This memo is added in your page")

            i = i + 1
        entry.bind("<Return>", showInput)
        print(entry.get())