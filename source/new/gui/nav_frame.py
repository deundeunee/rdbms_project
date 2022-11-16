from tkinter import ttk
import tkinter as tk
from about import About
from map import Map


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
        self.windows = {
            "About": "about",
            "Map": Map(parent),
            "News": "news",
            "Suggest": "suggest",
            "My Page": "my page",
        }
        button_texts = ["About", "Map", "News", "Suggest", "My page"]
        self.buttons = []
        idx = 1
        for button_text in button_texts:
            self.buttons.append(tk.Button(self, text=button_text, background="MistyRose"))
            self.buttons[idx - 1].grid(row=idx + 1, column=0, pady=10, sticky="nswe")
            idx += 1

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(len(button_texts) + 2, weight=1)
        i = 0
        for button in self.buttons:
            button.bind(
                "<Button-1>",
                lambda event, button=button_texts[i]: self.index_handler(event, button, parent),
            )
            i += 1

        self.clear_top_middle(parent)
        About(parent).place(relwidth=1)
        parent.get_frame("main").top_frame.create_title_label("About", ("Arial", 20))

    def index_handler(self, event, button, parent):
        self.clear_top_middle(parent)
        main = parent.get_frame("main")
        main.top_frame.create_title_label(button, ("Arial", 20))

        for b in self.buttons:
            b.configure(background="MistyRose")
            if button == b.cget("text"):
                b.configure(background="#F1948A")

        if button == "Map":
            Map(parent).place(relwidth=1)
        elif button == "About":
            About(parent).place(relwidth=1)

    def clear_top_middle(self, parent):
        main = parent.get_frame("main")

        for widget in main.top_frame.winfo_children():
            widget.destroy()
        for widget in main.middle_frame.winfo_children():
            widget.destroy()
