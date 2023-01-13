# url_doc_ibge = 'https://www.gov.br/conecta/catalogo/apis/metadados-estatisticos-do-ibge/ibge-metadados-manual-json/swagger_view'
# url_doc_portal_transparencia = 'https://api.portaldatransparencia.gov.br/swagger-ui.html#/'

import requests
import pandas as pd

sem_dados = '[]'
pagina = 1
url = 'https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siafi?pagina={}'.format(pagina)
headers = {
        'Content-Type': 'application/json',
        'chave-api-dados' : '249d215e1b35a32d5f9e0f90aadc9052'
    }
print('Lendo página nº{}'.format(pagina))
orgaos = requests.get(url, headers = headers)
dados = pd.read_json(orgaos.text)

while orgaos.text != sem_dados:
    pagina = pagina + 1
    print('Lendo página nº{}'.format(pagina))
    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siafi?pagina={}'.format(pagina)
    orgaos = requests.get(url, headers = headers) 
    adicionar_dados = pd.read_json(orgaos.text)
    dados = pd.concat([dados, adicionar_dados])
    dados = dados.reset_index(drop = True)
else:
    print('Acabou!')
    
print(len(dados['codigo']))