import requests
from bs4 import BeautifulSoup

companies = ['PAKRI','POL','PPL','SYS','UBL','GTECH','OGDC','MTL','MCB','HUBC','HINOON','EPCL','EFERT','DAWH','AVN']

page = requests.get("https://dps.psx.com.pk/company/POL")
soup = BeautifulSoup(page.content, 'html.parser')

share_price = soup.find_all('div', class_='stats_item')[0:3]
current_price = soup.find_all('div', class_='quote__close')


for value in share_price:
    print(value.text)

for value1 in current_price:
    print(value1.text)
