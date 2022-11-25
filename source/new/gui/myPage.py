from tkinter import ttk
import tkinter as tk


class myPage(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame

    def display(self, result):
        for res in result:
            label = tk.Label(self.middle_frame, text=res, bg="white")
            label.pack(pady=5)
