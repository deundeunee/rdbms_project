from tkinter import *
from PIL import ImageTk, Image
from test import printCommand

# Create a window
window = Tk()
window.geometry("700x500")
window.resizable()

# Background
bg_image = ImageTk.PhotoImage(Image.open("C:/Users/kb464/Pictures/landscape.jpg"))

bg_label = Label(image=bg_image)
bg_label.place(relwidth=1, relheight=1)


# Frame
frame = Frame(window, bg="#80c1ff", border=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor=N )

# Lower Frame
lower_frame = Frame(window, bg="#80c1ff", border=5)
lower_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor=N )

# Button
def button_click(store, addr):
    result = printCommand("SELECT 상호명,도로명주소 FROM original_shop_seoul WHERE ((상호명 like '%"+store+"%') and (시군구명 = '"+addr+"')) limit 10")
    string = "Store entered is " + store + " and addr entered is "+ addr
    
    for row in result:
        display = Text(lower_frame, height=1, )
        display.insert(END, row) 
        display.pack()

    print(string)

button = Button(frame, text = "Enter", command=lambda: button_click(store_entry.get(), addr_entry.get()), font=36)
button.place(anchor=NW, relwidth=0.2, relheight=1, relx=0.8)

# Lower Frame Label
label = Label(lower_frame, bg="white")
label.place(relheight=1, relwidth=1)

# Text entry
store_entry = Entry(frame, font=36)
store_entry.place(relwidth=0.5, relheight=1)

addr_entry = Entry(frame, font=36)
addr_entry.place(relwidth=0.25, relheight=1, relx=0.525)

# Loop
window.mainloop()