from tkinter import ttk
import tkinter as tk

import requests
from bs4 import BeautifulSoup


response = requests.get("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=spc")
soup = BeautifulSoup (response.text , 'html.parser')
news_group = soup.select_one('div.group_news')
news_title = news_group.find_all(class_='news_tit')
news_info = news_group.find_all('span', class_='info')
news_list = []
for i in range (len(news_title)):
    news_list.append(news_title[i].get_text()+'\n'+ news_title[i]['href']+'\n'+news_info[i].get_text())

print(news_list)
# for info in news_info:
    # print(info.get_text())

print("number of news titles", len(news_title))
for news in news_title:
    title = news.get_text()
    # print(title)

    url = news["href"]
    # print(url,'\n')

class News(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame


        for news in news_list:
            label = tk.Label(middle_frame, text=news, bg="white")
            label.pack(pady=5)

