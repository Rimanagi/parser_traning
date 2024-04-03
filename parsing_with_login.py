# beautifulsoup4 - поиск интересующих блоков в html коде веб-страницы
# lxml - парсер, помогает анализировать полученный код из request и подготавливает его в удобочитаемый вид
# вместо него можно использовать 'html.parser', но lxml быстрее и удобнее (вроде как)

from requests import Session
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

session = Session()

url = 'https://quotes.toscrape.com/'
session.get(url=url, headers=headers)

response = session.get('https://quotes.toscrape.com/login', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

form_data = {
    'csrf_token': token,
    'username': 'log',
    'password': 'pas',
}

session.post('https://quotes.toscrape.com/login', headers=headers, data=form_data, allow_redirects=True)
