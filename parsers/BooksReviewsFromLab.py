import time
import urllib.request
import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def makeFolder(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def GetHtmlFromPage(url, inInput):
    try:
        options = Options()
        books_names = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        chromedriver = r'D:/Projects/YandexLyceum/Parser/Selenium/Drivers/chromedriver.exe'
        options.binary_location = 'C:/Users/User/AppData/Local/NetboxBrowser/Application/netboxbrowser.exe'
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
        driver.get(url)
        try:
            driver.find_element_by_xpath('//div[@data-product-id]/div/div/div/a').click()
        except:
            driver.find_element_by_xpath('//a.cover').click()
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        rating = soup.find('div', {'id': 'rate'}).text
        # try:
        #     description = soup.find('span', {'class': "description"}).find('span', {'class': 'value-title'}).get('title')
        # except:
        #     description = soup.find('div', {'id': 'fullannotation'}).find('p').text
        # makeFolder(f"D:/Projects/YandexLyceum/BookBot/books/{inInput}")
        with open(f"D:/Projects/YandexLyceum/BookBot/books/{inInput}/description.txt", "a") as f:
            f.write('\n' + rating)
        # image = soup.find('div', {'id': 'product-image'}).find('img').get('src')
        # urllib.request.urlretrieve(image, f"D:/Projects/YandexLyceum/BookBot/books/{inInput}/image.png")
        driver.close()
    except:
        print(f"{inInput}")


with open('D:/Projects/YandexLyceum/Parser/files/Найденные.txt', 'r', encoding='utf-8') as f:
    names = f.readlines()
    for i in names:
        if '|' in i:
            GetHtmlFromPage(f"https://www.labirint.ru/search/{i}", i[:i.index(" |")])
        else:
            GetHtmlFromPage(f"https://www.labirint.ru/search/{i}", i[:-1])
