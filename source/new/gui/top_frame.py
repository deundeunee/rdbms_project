import tkinter as tk
from tkinter import ttk
import tkintermapview

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
        ).place(relheight=1, relwidth=1)

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

    def create_text_entry(self, frame):
        # Q14. Search function
        self.text_entry = tk.Entry(self)
        self.text_entry.pack(side=tk.BOTTOM, pady=10)

    def get_text_entry(self):
        return self.text_entry
