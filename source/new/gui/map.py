import tkinter as tk
from tkinter import ttk
import tkintermapview

from optionMenu import OptionMenuSet
from connection import button_click


class Map(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame
        middle_frame.config(padx=0)

        search_frame = tk.Frame(middle_frame, bg="lavender", padx=10, pady=10)
        search_frame.place(relwidth=1, relheight=0.1)
        self.search_widget(search_frame)

        self.addr_frame = tk.Frame(middle_frame, bg="white", padx=10, pady=10)
        self.addr_frame.place(relwidth=0.3, relheight=0.9, rely=0.1, x=10, anchor="nw")

        map_frame = tk.Frame(middle_frame, bg="lavender", padx=10)
        map_frame.place(relwidth=0.7, relheight=0.9, relx=0.3, rely=0.1)

        map_border = tk.Frame(map_frame, bg="green", padx=3, pady=3)
        map_border.pack(ipadx=3, ipady=3)

        w = int(map_frame.winfo_screenwidth() * 0.8 + 10)
        h = int(map_frame.winfo_screenheight())

        self.map_widget = tkintermapview.TkinterMapView(map_border, width=w, height=h)
        self.map_widget.pack(padx=(0, 0))
        # map_widget.set_position(37.588227,126.993606) # SKKU address
        # map_widget.set_address("25-2 Sungkyunkwan-ro, Jongno-gu, Seoul") # SKKU seoul campus
        # map_widget.set_address("Gyeonggi-do, Suwon-si, Jangan-gu, Cheoncheon-dong, 서부로 2066")
        self.map_widget.set_address("서울특별시 종로구 성균관로 25-2", marker=True).set_text("성균관대 인문캠")
        self.map_widget.set_zoom(15)
        self.map_widget.pack()

    def search_widget(self, frame):
        addr_label_frame = tk.Frame(frame)
        addr_label_frame.place(relwidth=0.2, relheight=1)

        option = OptionMenuSet(addr_label_frame)

        text_entry = tk.Entry(frame)
        text_entry.place(relwidth=0.69, relheight=1, relx=0.21)
        button = tk.Button(
            frame,
            text="Search",
            padx=10,
            command=lambda: button_click(
                text_entry.get(),
                option.get_gu(),
                option.get_dong(),
                self.addr_frame,
                self.map_widget,
            ),
        )
        button.place(
            relwidth=0.09,
            relheight=1,
            relx=0.91,
        )
