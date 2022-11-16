import tkinter as tk
from tkinter import ttk
import tkintermapview

from controller import (connectDB, build_sql_query, executeCommand)

# Create top, middle, and bottom frames
class BaseFrames(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        style = ttk.Style()
        style.configure("nav.TFrame", background="pink", )
        self.navigate_frame = NavFrame(parent, style="nav.TFrame" )
        self.navigate_frame.place(relwidth=0.15, relheight=1)

        self.main_frame = tk.Frame(parent, bg="white")
        self.main_frame.place(relwidth=0.85, relheight=1, relx=0.15)

        self.init_frames(self.main_frame)
        self.navigate_frame.create_index(self)
        
        self.sidebar_indicator = tk.Frame(self, background="#FFFFFF")

    def init_frames(self, parent):
        # Create a top frame
        style = ttk.Style()
        style.configure("top.TFrame", padding=10, background="white")

        self.top_frame = TopFrame(parent, style="top.TFrame")
        self.top_frame.place(relwidth=1, relheight=0.1)

        # Create a second frame middle_frame
        self.middle_frame = tk.Frame(parent, bg="azure", pady=10, padx=10)
        self.middle_frame.place(relwidth=1, relheight=0.8, rely=0.1)

        # Create a third frame bottom_frame
        self.bottom_frame = tk.Frame(parent, padx=10, pady=10, background="white")
        self.bottom_frame.place(relwidth=1, relheight=0.1, rely=0.9)

        # Clear button clears middle frame
        clear_button = tk.Button(self.bottom_frame, text="Clear")
        clear_button.pack(side=tk.RIGHT, anchor=tk.S)
        clear_button.bind(
            "<Button-1>",
            lambda event, frame=self.middle_frame: clear_frame(
                event, frame, self.get_frame("top").get_text_entry()
            ),
        )

    def get_frame(self, frame):
        if frame == "top":
            return self.top_frame
        elif frame == "middle":
            return self.middle_frame
        elif frame == "nav":
            return self.navigate_frame
        elif frame == "main":
            return self.navigate_frame


    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

class NavFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Title
        ttk.Label(
            self,
            text="PlaceToGo",
            font=("Arial", 20, "bold"),
            background="pink",
            padding=20,
            anchor="center"
        ).grid(row=0)

    def create_index(self, parent):
        # Index
        button_texts = ["About", "Map", "News", "Suggest", "My Page"]
        buttons = []
        idx = 1
        for button_text in button_texts:
            buttons.append(tk.Button(self, text=button_text))
            buttons[idx - 1].grid(row=idx+1, column=0, padx=5, pady=10)
            idx += 1

        self.grid_rowconfigure(len(button_texts)+2, weight=1)

        frame = parent.get_frame("middle")
        buttons[0].bind(
            "<Button-1>", lambda event, button="View Rentals": onclick_views(event, button, frame)
        )
        buttons[1].bind(  
            "<Button-1>",
            lambda event, button="Map": onclick_views(event, button, frame),
        )
        buttons[2].bind("<Button-1>", open_window)  # Q12. Button "Return Rentals"

# Widgets in a top frame
class TopFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = ttk.Label
        self.text_entry = ttk.Entry

    def create_title_label(self, title, font):
        # Q2.1. Put a label
        self.label = ttk.Label(
            self,
            text=title,
            font=font,
            background="white",
            anchor="center",
        ).place(relheight=0.7, relwidth=1)

    def create_buttons(self, parent):
        # Q2.2. Create 3 buttons
        button_texts = ["View Rentals", "Overdue Rentals", "Return Rentals"]
        buttons = []
        idx = 1
        for button_text in button_texts:
            buttons.append(tk.Button(self, text=button_text))
            buttons[idx - 1].grid(row=1, column=idx, padx=5, pady=10)
            idx += 1

        # Q6. Top_frame remain relatively centered when window is resized
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)

        frame = parent.get_frame("middle")
        buttons[0].bind(  # Q7.Button "View Rentals"
            "<Button-1>", lambda event, button="View Rentals": onclick_views(event, button, frame)
        )
        buttons[1].bind(  # Q10. Button "Overdue Rentals"
            "<Button-1>",
            lambda event, button="Overdue Rentals": onclick_views(event, button, frame),
        )
        buttons[2].bind("<Button-1>", open_window)  # Q12. Button "Return Rentals"

    def create_text_entry(self, frame):
        # Q14. Search function
        self.text_entry = tk.Entry(self)
        self.text_entry.bind(
            "<Return>",
            lambda event, button="Return Rentals", entry=self.text_entry: onclick_views(
                event, button, frame, entry
            ),
        )
        self.text_entry.pack(side=tk.BOTTOM, pady=10)

    def get_text_entry(self):
        return self.text_entry

class Map(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = ttk.Label
        self.text_entry = ttk.Entry
        map_widget = tkintermapview.TkinterMapView(parent, width=800, height=600)
        #map_widget.set_position(37.588227,126.993606) # SKKU address
        #map_widget.set_address("25-2 Sungkyunkwan-ro, Jongno-gu, Seoul") # SKKU seoul campus
        #map_widget.set_address("Gyeonggi-do, Suwon-si, Jangan-gu, Cheoncheon-dong, 서부로 2066")
        map_widget.set_address("서울특별시 종로구 성균관로 25-2", marker=True).set_text("성균관대 인문캠")
        map_widget.set_zoom(15)
        map_widget.pack()
        
# Open second window
def open_window(event):  
    top = tk.Toplevel()
    top.title("Return Rental")
    top.geometry("600x500")
    base = BaseFrames(top)

    top_frame = base.get_frame("top")  
    middle_frame = base.get_frame("middle")
    top_frame.create_title_label("Enter customer name", ("Arial,", 11))
    top_frame.create_text_entry(middle_frame)



# Clear all widgets in a frame
def clear_frame(event, frame, entry=None):
    for widget in frame.winfo_children():
        widget.destroy()
    if entry == tk.Entry:  # Q15. Clear button clears text entry field
        entry.delete(0, "end")


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

            # Q14.2 "Return" button for every row
            if title == "Customer Rentals" and col == len(res) - 1:
                button = tk.Button(
                    frame, text="Return", anchor="w", command=lambda data=res: update_data(data)
                )
                button.grid(row=idx, column=col + 2)
        idx += 1

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(len(res) + 1, weight=1)


# Q17. Update the return_date and display a pop-up
def update_data(data):
    rental_id = data[0]
    mydb, mycursor = connectDB("sakila")
    command = "UPDATE rental SET return_date = NOW() WHERE rental_id={}".format(rental_id)
    tk.messagebox.showinfo("Confirm", "The rental has been returned!")
    executeCommand(mydb, mycursor, command)


# Button listner
def onclick_views(event, button, frame, entry=None):
    # Clear middle_frame before displaying
    clear_frame(event, frame)
    # Make connection to DB
    mydb, mycursor = connectDB("sakila")

    # Q7.
    if button == "Map":
        Map(frame).pack()
    elif button == "View Rentals":
        fields = ["film_id", "title", "rental_rate"]
        command = build_sql_query(fields, "film")
        result = executeCommand(mydb, mycursor, command)
        fields[2] = "rate"
        title_label_text = "Viewing Rentals"
        font = ("Arial", 11)
    # Q10.
    elif button == "Overdue Rentals":
        fields = [
            "rental.customer_id",
            "CONCAT(customer.first_name, ',', customer.last_name) AS customer",
            "address.phone",
            "rental.rental_id",
            "film.title",
        ]
        table = """rental INNER JOIN customer ON rental.customer_id = customer.customer_id
           INNER JOIN address ON customer.address_id = address.address_id
           INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
           INNER JOIN film ON inventory.film_id = film.film_id"""
        conditions = """rental.return_date IS NULL ORDER BY rental_id"""
        command = build_sql_query(fields, table, conditions)
        result = executeCommand(mydb, mycursor, command)

        # create view
        fields[1] = "rental.customer"
        fields = [field.split(".")[1] for field in fields]
        title_label_text = "Overdue Customer Rentals"
        font = ("Arial", 9)

    # Q14. Search overdue films with customer name
    elif button == "Return Rentals":
        input_name = entry.get()
        fields = [
            "rental.rental_id",
            "rental.customer_id",
            "rental.rental_date",
        ]
        table = "rental INNER JOIN customer ON rental.customer_id = customer.customer_id"
        condition = (
            "(customer.first_name LIKE '%"
            + input_name
            + "%' OR customer.last_name LIKE '%"
            + input_name
            + "%') AND rental.return_date IS NULL "
        )
        command = build_sql_query(fields, table, condition)
        result = executeCommand(mydb, mycursor, command)
        fields = [field.split(".")[1] for field in fields]
        fields.append("update")
        title_label_text = "Customer Rentals"
        font = ("Arial", 9)

    # Q14.1. Display a message if there is no record
    if result and len(result) != 0:
        display_table(frame, title_label_text, fields, result, font)
    else:
        no_record_label = tk.Label(
            frame,
            text="User '" + input_name + "' does not have any overdue rentals",
            font=("Arial", 11),
            background="azure",
        )
        no_record_label.place(relwidth=1, relheight=1)

    # Close the connection
    mydb.close()


# PART 1. GUI Layout
# Q1. Create a window with the title and the size
window = tk.Tk()
window.geometry("1280x720")
window.title("PlaceToGo - boycott helper")

base = BaseFrames(window)

# top_frame = base.get_frame("top")
# top_frame.create_title_label("Welcome to Sakila Rental System", ("Arial,", 20))
# top_frame.create_buttons(base)


# Keep the application object in a loop.
window.mainloop()
