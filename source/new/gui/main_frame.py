import tkinter as tk
from tkinter import ttk

from top_frame import TopFrame


class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_frames()

    def init_frames(self):
        # Create a top frame
        style = ttk.Style()
        style.configure("top.TFrame", padding=10, background="white")

        self.top_frame = TopFrame(self, style="top.TFrame")
        self.top_frame.place(relwidth=1, relheight=0.1)

        # Create a second frame middle_frame
        self.middle_frame = tk.Frame(self, bg="lavender", pady=10, padx=10)
        self.middle_frame.place(relwidth=1, relheight=0.8, rely=0.1)

        # Create a third frame bottom_frame
        self.bottom_frame = tk.Frame(self, padx=10, pady=10, background="white")
        self.bottom_frame.place(relwidth=1, relheight=0.1, rely=0.9)
