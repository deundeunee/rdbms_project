from tkinter import ttk
import tkinter as tk
from map import Map


class About(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame

        label = tk.Label(middle_frame, text="This application is to help you...", bg="white")
        label.pack()
