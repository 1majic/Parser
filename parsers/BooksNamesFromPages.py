import time
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def ParseBooksNamesFromPage(url):
    options = Options()
    books_names = []
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
          }
    # url = 'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/'
    chromedriver = r'D:/Projects/YandexLyceum/Parser/Selenium/Drivers/chromedriver.exe'
    options.binary_location = 'C:/Users/User/AppData/Local/NetboxBrowser/Application/netboxbrowser.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    # html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, features="html.parser")
    book_list = soup.find_all('span', {'class': 'j4 as3 az a0f2 f-tsBodyL item b3u9'})
    for i in book_list:
        books_names.append(i.find('span').text)
    return "\n".join(books_names)


Pages = ['https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/',
         'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/?page=2',
         'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/?page=3',
         'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/?page=4',
         'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/?page=5',
         'https://www.ozon.ru/highlight/top-200-knig-po-mneniyu-chitateley-ozon-22872/?page=6'
         ]
for i in Pages:
    print(ParseBooksNamesFromPage(i))




