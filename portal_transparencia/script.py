import requests
import pandas as pd

# url_doc_ibge = 'https://www.gov.br/conecta/catalogo/apis/metadados-estatisticos-do-ibge/ibge-metadados-manual-json/swagger_view'
# url_doc_portal_transparencia = 'https://api.portaldatransparencia.gov.br/swagger-ui.html#/'

tabela = pd.read_csv('portal_transparencia\_arquivos\codigoorgao.csv')
print(tabela)

url = 'https://api.portaldatransparencia.gov.br/api-de-dados/notas-fiscais?codigoOrgao=52111&pagina=1'
headers = {
    'Content-Type': 'application/json',
    'chave-api-dados' : '249d215e1b35a32d5f9e0f90aadc9052'
}

nf = requests.get(url, headers = headers)