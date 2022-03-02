from bs4 import BeautifulSoup
import requests


website = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
ls= list()
news= list()
ls =  [item.get_text(strip = True) for item in soup.select('p', class_='font-copy font--article-body gray-darkest ma-0 pb-md')]

    
for i in ls:
    if i != '':
        news.append(i)
print(news) 
