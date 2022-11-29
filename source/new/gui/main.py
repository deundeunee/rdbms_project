import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from main_frame import MainFrame
from nav_frame import NavFrame
from connection import *
from login import Login

# Create top, middle, and bottom frames
class BaseFrames(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        style = ttk.Style()
        style.configure(
            "nav.TFrame",
            background="pink",
        )
        style.configure(
            "main.TFrame",
            background="white",
        )

        self.navigate_frame = NavFrame(parent, style="nav.TFrame")
        self.navigate_frame.place(relwidth=0.15, relheight=1)

        self.main_frame = MainFrame(parent, style="main.TFrame")
        self.main_frame.place(relwidth=0.85, relheight=1, relx=0.15)

        self.user_id, self.password = tk.StringVar(), tk.StringVar()

        Login(self).place(relwidth=1)

    def get_frame(self, frame):
        if frame == "top":
            return self.main_frame.top_frame
        elif frame == "middle":
            return self.main_frame.middle_frame
        elif frame == "nav":
            return self.navigate_frame
        elif frame == "main":
            return self.main_frame


window = tk.Tk()
window.geometry("1280x720")
window.title("PlaceToGo - boycott helper")

base = BaseFrames(window)

# Keep the application object in a loop.
window.mainloop()
