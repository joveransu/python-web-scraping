import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_name = str(input('Qual produto deseja? ')).strip()

response = requests.get(url_base + produto_name)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={
                        'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

total_pesquisa = 0
for produto in produtos:
    total_pesquisa += 1
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})
    if not centavos:
        centavos = '00'

    promo = produto.find(
        'div', attrs={'class': 'ui-search-price__second-line'})

    real_promo = promo.find('span', attrs={'class': 'price-tag-fraction'})
    centavos_promo = promo.find('span', attrs={'class': 'price-tag-cents'})
    if not real_promo:
        real_promo = real
    if not centavos_promo:
        centavos_promo = centavos

    link = produto.find(
        'a', attrs={'class': 'ui-search-item__group__element ui-search-link'})

    resultado = f'''Produto: {titulo.text}
Preço de: {real.text},{centavos.text}
Por: {real_promo.text},{centavos_promo.text}
Link: {link["href"]}'''

    print('\033[93m-=\033[m' * 40)
    print(resultado)

print('\n\n')
print('\033[93m-=\033[m' * 40)
print(f'Foram encontrados {total_pesquisa} resultados.')
