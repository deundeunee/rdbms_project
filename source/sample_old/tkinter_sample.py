from tkinter import *
from PIL import ImageTk, Image
from connection import printCommand


class OptionMenuSet(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.gu_dong_dict = dict()

        gus = printCommand("select distinct 시군구명 from addr_view")
        for gu in gus:
            dongs_org = printCommand(
                "select distinct 법정동명 from addr_view where 시군구명='" + gu[0] + "' order by 법정동명"
            )
            dongs = [dong[0] for dong in dongs_org]
            self.gu_dong_dict[gu[0]] = dongs

        print(self.gu_dong_dict)

        self.variable_a = StringVar(self)
        self.variable_b = StringVar(self)
        self.variable_a.trace("w", self.update_options)

        self.optionmenu_a = OptionMenu(self, self.variable_a, *self.gu_dong_dict.keys())
        self.optionmenu_b = OptionMenu(self, self.variable_b, "")

        self.variable_a.set("강남구")

        self.optionmenu_a.grid(row=0, column=0)
        self.optionmenu_b.grid(row=0, column=1)
        self.pack()

    def update_options(self, *args):
        countries = self.gu_dong_dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.optionmenu_b["menu"]
        menu.delete(0, "end")

        for country in countries:
            menu.add_command(
                label=country, command=lambda nation=country[0]: self.variable_b.set(nation)
            )


# Create a window
window = Tk()
window.geometry("700x800")
window.resizable()


# Frame
frame = Frame(window, bg="#80c1ff", border=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor=N)

# Lower Frame
lower_frame = Frame(window, bg="#80c1ff", border=5)
lower_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor=N)

# Button
def button_click(store, addr):
    result = printCommand(
        "SELECT 상호명,도로명주소 FROM original_shop_seoul WHERE ((상호명 like '%"
        + store
        + "%') and (시군구명 = '"
        + addr
        + "')) limit 10"
    )
    string = "Store entered is " + store + " and addr entered is " + addr

    for row in result:
        display = Text(
            lower_frame,
            height=1,
        )
        display.insert(END, row)
        display.pack()

    print(string)


button = Button(
    frame, text="Enter", command=lambda: button_click(store_entry.get(), addr_entry.get()), font=36
)
button.place(anchor=NW, relwidth=0.2, relheight=1, relx=0.8)

# Lower Frame Label
label = Label(lower_frame, bg="white")
label.place(relheight=1, relwidth=1)

# Text entry
store_entry = Entry(frame, font=36)
store_entry.place(relwidth=0.5, relheight=1)

addr_entry = Entry(frame, font=36)
addr_entry.place(relwidth=0.25, relheight=1, relx=0.525)

OptionMenuSet(window)
# option = StringVar()
# option.set(items[0])  # default value
# drop_gu = OptionMenu(frame, option, *items, command=lambda data=option.get(): show(data))
# drop_gu.pack()


# Loop
window.mainloop()
