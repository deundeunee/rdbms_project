from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


driver = set_chrome_driver()
driver.get("https://www.paris.co.kr/store/")  # 파리바게트 홈페이지

# 페이지가 완전히 로딩되도록 3초동안 기다림
driver.implicitly_wait(3)

driver.find_element(
    By.XPATH, '//*[@id="main"]/div[1]/div[1]/div[1]/ul/li[2]/a'
).click()  # '검색해서 찾기' 클릭
driver.find_element(
    By.XPATH, '//*[@id="main"]/div[1]/div[1]/div[1]/div/form/div[2]/div[1]/div/div[2]/span'
).click()  # '도/시 선택' 클릭
driver.find_element(
    By.XPATH,
    '//*[@id="main"]/div[1]/div[1]/div[1]/div/form/div[2]/div[1]/div/div[3]/div/div[1]/ul/li[10]',
).click()  # '서울' 클릭
driver.implicitly_wait(10)

cards = driver.find_elements(By.CLASS_NAME, "store-list-item.show-timetable")  # list 요소들
len = len(cards)  # list 길이 (서울에 있는 파리바게뜨는 약 700개)

# csv 파일 생성을 위한 변수
headers = ["store_title", "store_addr"]
store_title_list = []
store_addr_list = []

# list 길이만큼 반복하며 파리바게트 지점명, 주소 받아오기
for i in range(1, len):
    path = '//*[@id="store_list"]/ul/li[{}]'.format(i)  # 지점명, 주소가 있는 요소의 XPATH
    # 지점명
    store_title_path = path + "/div/h3/span"
    store_title = "파리바게뜨 " + driver.find_element(By.XPATH, store_title_path).text
    # 주소
    store_addr_path = path + "/div/p[1]"
    store_addr = driver.find_element(By.XPATH, store_addr_path).text
    # 리스트에 추가
    store_title_list.append(store_title)
    store_addr_list.append(store_addr)
    # 확인을 위한 출력
    print("{0:20}\t{1}".format(store_title, store_addr))

# 지점명, 지점 주소를 짝을 지음. 하나의 행으로 만들기 위함
ziplist = zip(store_title_list, store_addr_list)

# csv 파일 생성
with open("parisbaguette.csv", "w", newline="") as file:
    write = csv.writer(file)
    write.writerow(headers)
    write.writerows(ziplist)

# csv 파일 내용 예시
# 파리바게뜨 신이문역,서울특별시 동대문구 신이문로25길 1
# 파리바게뜨 답십리위브,서울특별시 동대문구 답십리로 130 근생동 1-5호
# 파리바게뜨 세종대,서울특별시 광진구 군자동 98번지 세종대학교 내학생회관1층
# 파리바게뜨 외대후문,서울특별시 동대문구 천장산로7길 4 지층 1층
# 파리바게뜨 묵동삼거리,서울 중랑구 공릉로 2길 3
# 파리바게뜨 경희대,서울 동대문구 경희대로 8-1
