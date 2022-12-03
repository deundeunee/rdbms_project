import requests
response = requests.get("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=spc")

from bs4 import BeautifulSoup
soup = BeautifulSoup (response.text , 'html.parser')
news = soup.select_one('div.group_news')
newslist = news.find_all(class_='news_tit')

print("number of news titles", len(newslist))
for news in newslist:
    title = news.get_text()
    print(title)

    url = news["href"]
    print(url,'\n')


    