# url_doc_ibge = 'https://www.gov.br/conecta/catalogo/apis/metadados-estatisticos-do-ibge/ibge-metadados-manual-json/swagger_view'
# url_doc_portal_transparencia = 'https://api.portaldatransparencia.gov.br/swagger-ui.html#/'

import requests
import pandas as pd

tabela = pd.read_json('portal_transparencia\_arquivos\lista_orgao.json')
consulta = 0
dados = ''

while consulta <= 24:
    sem_dados = '[]'
    pagina = 1
    codigo_orgao = tabela['codigo_orgao'][consulta]
    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao={}&pagina={}'.format(codigo_orgao, pagina)
    headers = {
        'Content-Type': 'application/json',
        'chave-api-dados' : '249d215e1b35a32d5f9e0f90aadc9052'
    }

    nf = requests.get(url, headers = headers)
    
    while nf.text != sem_dados:
        print('Armazenando dados do orgão nº{} da página nº{}[...]'.format(codigo_orgao, pagina))
        dados = dados + nf.text
        print('Dados foram armazenados com sucesso!')
        pagina = pagina + 1
        url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao={}&pagina={}'.format(codigo_orgao, pagina)
        nf = requests.get(url, headers = headers)
    else:
        print('Não há dados no orgão nº{} na página nº{}.'.format(codigo_orgao, pagina))
        consulta = consulta + 1
        
arquivo_json = open('portal_transparencia\_arquivos\dados_nf.json', 'w', encoding = 'utf-8')
arquivo_json.write(dados.replace('][', ','))