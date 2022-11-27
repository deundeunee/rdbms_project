from tkinter import messagebox, ttk
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from connection import *


response = requests.get(
    "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=spc"
)
soup = BeautifulSoup(response.text, "html.parser")
news_group = soup.select_one("div.group_news")
news_title = news_group.find_all(class_="news_tit")
news_info = news_group.find_all("span", class_="info")
news_list = []
for i in range(len(news_title)):
    news_list.append(
        news_title[i].get_text() + "\n" + news_title[i]["href"] + "\n" + news_info[i].get_text()
    )

# print(news_list)
# for info in news_info:
# print(info.get_text())

print("number of news titles", len(news_title))
for news in news_title:
    title = news.get_text()
    # print(title)

    url = news["href"]
    # print(url,'\n')

# 데이터 프레임으로 만들어서 SQL로 넣기
db, cursor = connectDB("project")
#
# def number (k):


class News(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=2)
        for k, news in enumerate(news_list):
            label2 = tk.Label(middle_frame, text=news, bg="white", pady=5)
            label2.grid(row=k, column=1, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
            button = tk.Button(
                middle_frame,
                text="Add",
                height=3,
                width=5,
                activebackground="red",
                command=lambda k=k: add_click(k),
            )
            button.grid(row=k, column=2, padx=5)


def add_click(k):
    cursor.execute(
        "CREATE TABLE if not exists my_news(id INT AUTO_INCREMENT PRIMARY KEY, news_title VARCHAR(255), url VARCHAR(255))"
    )
    query = "insert into my_news (news_title, url) values (%s,%s)"
    cursor.execute(query, (news_title[k].get_text(), news_title[k]["href"]))
    db.commit()
    messagebox.showinfo("Success", "This news is added in your page")
    print(k)
