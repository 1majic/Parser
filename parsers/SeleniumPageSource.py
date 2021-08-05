import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def StartUrlDriver(url):
    options = Options()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    chromedriver = r'D:/Projects/YandexLyceum/Parser/Selenium/Drivers/chromedriver.exe'
    options.binary_location = 'C:/Users/User/AppData/Local/NetboxBrowser/Application/netboxbrowser.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
    driver.get(url)
    return driver


Page = StartUrlDriver('https://www.twitch.tv/')





