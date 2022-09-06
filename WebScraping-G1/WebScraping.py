'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.magazineluiza.com.br/selecao/ofertasdodia/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
page = requests.get(url, headers=headers)

site = BeautifulSoup(page.content, 'html.parser')
print(site)
respostas = site.findAll('div', {'class':'sc-iyyVIK gdPMEf'})
print(respostas)
for tags in respostas:
    titulo = tags.find('h2', {'class':'sc-iNpzLj kewvRW'})
    price_original = tags.find('p', {'class':'sc-kDTinF xepxx sc-itWPBs jVtgqI'})
    new_price = tags.find('p', {'class':'sc-kDTinF zuoFI sc-dcgwPl bvdLco'})
    print(titulo)
    print(price_original)
    print(new_price)
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

  # print(titulo.text)
  # print(titulo['href']) # link da notícia

  # Subtítulo: div class="feed-post-body-resumo"
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if (subtitulo):
    # print(subtitulo.text)
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    lista_noticias.append([titulo.text, '', titulo['href']])

for i in lista_noticias:
  print(i[0], i[1], i[2])


'''
news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])
news.to_excel(news)
try:
    arquivo = open('WebScraping/news.txt', 'r+')
except FileNotFoundError:
    arquivo = open('WebScraping/news.txt', 'w+')
    arquivo.write(str(news))
arquivo.close()
'''
