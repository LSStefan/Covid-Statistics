from bs4 import BeautifulSoup
import requests
from datetime import date

url = 'https://www.worldometers.info/coronavirus/'
number = []
today = str(date.today())
#search for each country
def show(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    number = soup.find_all('div',class_="maincounter-number")  #cases,deaths,recovered
    updates = soup.find('div',class_='news_post')
    new = updates.find('strong')
    print(f'TOTAL CASES: {number[0].text}\n')
    print(f'DEATHS: {number[1].text}\n')
    print(f'RECOVERED: {number[2].text}\n')
    print(f'UPDATES:{new.text}')
#global search
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')
number = soup.find_all('div',class_="maincounter-number")
print(f'TOTAL CASES: {number[0].text}\n')
print(f'DEATHS: {number[1].text}\n')
print(f'RECOVERED: {number[2].text}\n')
def printintxt(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    number = soup.find_all('div', class_="maincounter-number")
    file = open(today + '.txt', 'w')
    file.write(f'TOTAL CASES: {number[0].text}\n')
    file.write(f'DEATHS: {number[1].text}\n')
    file.write(f'RECOVERED: {number[2].text}\n')


print(f"Today date:{today}")
print('\n')
printintxt(url)
print('See the situation in a country(lowercase):')
while 1:
    url = 'https://www.worldometers.info/coronavirus/'
    country = str(input())
    if country == '0':
        break
    url = url + 'country/' + country + '/'
    show(url)
    print('Press 0 to exit')