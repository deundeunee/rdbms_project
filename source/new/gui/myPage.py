from tkinter import ttk
import tkinter as tk
from connection import *


class My_page(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=1)
        middle_frame.columnconfigure(2, weight=1)
        middle_frame.columnconfigure(3, weight=1)
        middle_frame.columnconfigure(4, weight=1)
        
        db, c = connectDB('project')

        c.execute("""
                        select * from my_store """) #user_id로 필터링 되는 코드 추가하기
        result = c.fetchall()
        # Label in top row
        label2 = tk.Label(middle_frame, text="YOUR PAGE", bg="white", font=("Arial", 14))
        label2.grid(row=0, column=2, columnspan=1)

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
                print(res[j])
                res_label = tk.Label(middle_frame, text=res[j], bg="white")
                res_label.grid(row=i, column=j)
            entry = tk.Entry(middle_frame)
            entry.grid(row=i, column=len(res))
            i = i + 1

    #     entry.bind("<Return>", showInput())
    #
    # def showInput(entry):
    #     query = """insert into my_store (memo) values %s """
    #     c.execute(query,entry)
    #     db.commit()