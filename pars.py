from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36"
}
work = Session()
work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"csrf_token": token, "username": "username", "password": "password"}

result = work.post(
    "https://quotes.toscrape.com/login",
    headers=headers,
    data=data,
    allow_redirects=True,
)


def arr_url():

    for count in range(1, 11):
        sleep(0.5)
        url = f"https://quotes.toscrape.com/page/{count}/"
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="quote")
        for i in data:
            quote = i.find("span", class_="text").text
            author = i.find("small", class_="author").text
            yield quote, author
            

