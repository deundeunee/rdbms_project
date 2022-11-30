from tkinter import *
from PIL import ImageTk, Image
from connection import executeCommand, connectDB


class OptionMenuSet(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        mydb, mycursor = connectDB("project")
        mycursor.execute(
            """
            CREATE OR REPLACE VIEW gu_dong AS
            SELECT DISTINCT 시군구명, 법정동명 
            FROM original_shop_seoul 
            GROUP BY 법정동명 
            ORDER BY 시군구명, 법정동명"""
        )
        mydb.commit()

        mycursor.execute("SELECT * from gu_dong")
        gu_dong_result = mycursor.fetchall()
        self.gu_dong_dict = {}
        for key, value in gu_dong_result:
            self.gu_dong_dict.setdefault(key, []).append(value)

        self.variable_gu = StringVar(self)
        self.variable_dong = StringVar(self)
        self.variable_gu.trace("w", self.update_options)

        self.optionmenu_gu = OptionMenu(self, self.variable_gu, *self.gu_dong_dict.keys())
        self.optionmenu_dong = OptionMenu(self, self.variable_dong, "")

        self.variable_gu.set("강남구")

        self.optionmenu_gu.grid(row=0, column=0)
        self.optionmenu_dong.grid(row=0, column=1)
        self.pack()

    def update_options(self, *args):
        dongs = self.gu_dong_dict[self.variable_gu.get()]
        self.variable_dong.set(dongs[0])

        menu = self.optionmenu_dong["menu"]
        menu.delete(0, "end")

        for dong in dongs:
            menu.add_command(label=dong, command=lambda nation=dong: self.variable_dong.set(nation))

    def get_gu(self):
        print(self.variable_gu.get())
        return self.variable_gu.get()

    def get_dong(self):
        print(self.variable_dong.get())
        return self.variable_dong.get()
