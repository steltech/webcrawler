import re
import requests


def get_url(url):
    requisicao = requests.get(url)
    padrao = re.findall(r'[\w\.-]+@[\w-]+.[\w\.-]+', requisicao.text)
    if padrao:
        return padrao
    return 'Padrao nao encontrado'


def get_html_links(url):
    ''' Retorna uma lista de links '''
    links = re.findall(r'href=[\'"]?([^\'" >]+)', url)
    return links


if __name__ == '__main__':
    URL = 'http://steltech.com.br/contato/'
    print(get_url(URL))
    print(get_html_links(URL))
