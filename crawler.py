import re
import requests

url = 'http://lacoxinha.com.br/contato'

requisicao = requests.get(url)

padrao = re.findall(r'[\w\.-]+@[\w-]+.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrao nao encontrado')