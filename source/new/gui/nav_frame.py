from tkinter import ttk
import tkinter as tk
from map import Map
from news import News
from myPage import My_page
from login import Login


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
            anchor="center",
        ).grid(row=0)

    def create_index(self, parent):
        # Index

        button_texts = ["Map", "News", "My page", "Log out"]
        self.buttons = []
        idx = 1
        for button_text in button_texts:
            self.buttons.append(tk.Button(self, text=button_text, background="MistyRose"))
            if idx != len(button_texts):
                self.buttons[idx - 1].grid(row=idx + 1, column=0, pady=10, sticky="nswe")
            else:
                self.buttons[idx - 1].grid(row=idx + 2, column=0, pady=10, sticky="we")
            idx += 1

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(len(button_texts) + 1, weight=1)
        i = 0
        for button in self.buttons:
            button.bind(
                "<Button-1>",
                lambda event, button=button_texts[i]: self.index_handler(event, button, parent),
            )
            i += 1

        self.clear_top_middle(parent)
        Map(parent).place(relwidth=1)
        self.buttons[0].configure(background="#F1948A")
        parent.get_frame("main").top_frame.create_title_label("Map", ("Arial", 20))

    def index_handler(self, event, button, parent):
        self.clear_top_middle(parent)
        main = parent.get_frame("main")
        main.top_frame.create_title_label(button, ("Arial", 20))

        for b in self.buttons:
            b.configure(background="MistyRose")
            if button == b.cget("text"):
                b.configure(background="#F1948A")

        # if button == "About":
        #     About(parent).place(relwidth=1)
        if button == "Map":
            Map(parent).place(relwidth=1)
        elif button == "News":
            News(parent).place(relwidth=1)
        # elif button == "Suggest":
        #     Suggest(parent).place(relwidth=1)
        elif button == "My page":
            My_page(parent).place(relwidth=1)
        elif button == "Log out":
            self.label = ttk.Label(
                parent.main_frame.middle_frame,
                text="Do you really want to Log out?",
                font=("Arial", 12),
                background="lavender",
                anchor="center",
            ).pack()

            def logout():
                for widget in self.winfo_children():
                    widget.destroy()
                ttk.Label(
                    self,
                    text="PlaceToGo",
                    font=("Arial", 20, "bold"),
                    background="pink",
                    padding=20,
                    anchor="center",
                ).grid(row=0)
                self.clear_top_middle(parent)
                Login(parent).place(relwidth=1)

            tk.Button(parent.main_frame.middle_frame, text="Log out", command=logout).pack()

    def clear_top_middle(self, parent):
        main = parent.get_frame("main")

        for widget in main.top_frame.winfo_children():
            widget.destroy()
        for widget in main.middle_frame.winfo_children():
            widget.destroy()
