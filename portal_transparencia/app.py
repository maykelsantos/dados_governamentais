import app_orgaos_siafi as orgaos_siafi
import requests
import pandas as pd

sem_dados = '[]'
pagina = 1
index_codigo = 0
codigo_orgao = orgaos_siafi.dados['codigo'][index_codigo]
total_codigo_orgao = len(orgaos_siafi.dados['codigo'])

for consulta in range(total_codigo_orgao):
    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao={}&pagina={}'.format(codigo_orgao, pagina)
    headers = {
        'Content-Type': 'application/json',
        'chave-api-dados' : '249d215e1b35a32d5f9e0f90aadc9052'
    }
    nf = requests.get(url, headers = headers)
    print('Trabalhando nos dados do Órgão {}'.format(codigo_orgao))
    
    if nf.text != sem_dados:
        dados = pd.read_json(nf.text)
        pagina = pagina + 1
        url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao={}&pagina={}'.format(codigo_orgao, pagina)
        nf = requests.get(url, headers = headers)
        dados = pd.concat([dados, dados])
        dados = dados.reset_index(drop = True)
        display(dados)
    else:
        index_codigo = index_codigo + 1
        codigo_orgao = orgaos_siafi.dados['codigo'][index_codigo]
        url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao={}&pagina={}'.format(codigo_orgao, pagina)
        nf = requests.get(url, headers = headers)