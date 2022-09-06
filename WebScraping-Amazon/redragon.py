import requests
from bs4 import BeautifulSoup

url_base = 'https://www.amazon.com.br/'
url = 'https://www.amazon.com.br/s?k='
#produto = 'Redragon Shiva'.replace(' ', '+')
req = str(input('Qual produto? ')).strip().replace(' ', '+')

response = requests.get(url+req)

while 'Response [503]' in str(response):
    response = requests.get(url+req)
    
if not 'Response [400]' in str(response):
    print('\033[35mErro, a requisição com o site não foi possivel.\033[m')
else:
    site = BeautifulSoup(response.content, 'html.parser')

    products = site.findAll('div', attrs={'class':'a-section a-spacing-base'})

    for product in products:
        titulo = product.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
        price = product.find('span', attrs={'class': 'a-offscreen'})
        link = product.find('a', attrs={'class':'a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        if not link:
            link = {'href':f"{str(titulo.text).replace(' ','+')}"}

        print('\033[93m-=\033[m' * 35)
        print(f"Nome do Produto: {titulo.text}")
        print(f"Preço: {price.text}")
        print(f"Link: {url_base + link['href']}")
        print('\033[93m-=\033[m\n' * 35)
