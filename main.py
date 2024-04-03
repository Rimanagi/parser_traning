# beautifulsoup4 - поиск интересующих блоков в html коде веб-страницы
# lxml - парсер, помогает анализировать полученный код из request и подготавливает его в удобочитаемый вид
# вместо него можно использовать 'html.parser', но lxml быстрее и удобнее (вроде как)
import requests
from bs4 import BeautifulSoup
from xl_creator import writer, xl_file


def download(url):
    # stream=True потоковое скачивание, а не разом
    response = requests.get(url, stream=True)
    # b - write in bytes
    with open(f'/Users/rimanagi/PycharmProjects/Parsing_orscraping_sites/downloaded_images/{url.split("/")[-1]}', 'wb') as file:
        for value in response.iter_content(1024 * 1024):  # 1Mb
            file.write(value)

    pass


url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)

# response.text - вернет html документ | BeautifulSoup - распарсит html текст с помощью 'lxml' | 'html.parser'
soup = BeautifulSoup(response.text, 'lxml')

# Вернет список строк, где каждый эл-т содержание указанного тега с атрибутами
cards = soup.find_all('div', attrs={'class': 'w-full rounded border'})

row = 0
for card in cards:
    name = card.find('h4').text.replace('\n', '')
    price = soup.find('h5').text.replace('\n', '')
    img_url = 'https://scrapingclub.com' + card.find('img').get('src')

    # find - позволяет получить содержимое всего тега | get - позволяет получить содержимое атрибута
    product_link = 'https://scrapingclub.com' + card.find('a').get('href')
    response_product = requests.get(product_link)
    soup_product = BeautifulSoup(response_product.text, 'lxml')
    description = soup_product.find('p', attrs={'class': "card-description"}).text


    # writer(name, price, product_link, description, row)
    download(img_url)
    row += 1
    print(name, price, sep='\n')
    print(product_link)
    print(description,)
    print(img_url)
    print('\n')

xl_file.close()
