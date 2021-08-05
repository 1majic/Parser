import requests
from bs4 import BeautifulSoup

search = input("книга: ")
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
html = requests.get("http://flibusta.is/booksearch?ask="+search, proxies=proxies).text
print("получен ответ")
soup = BeautifulSoup(html, features="html.parser")
book_link = soup.find("ul").find("li")
for i in book_link:
    book = i.find_next("a")
    print(book)


