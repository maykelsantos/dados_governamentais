import pandas as pd

base_dados = pd.read_json('portal_transparencia\_arquivos\dados_nf.json')

# nome das colunas
c_id = 'id'
c_codigoOrgaoSuperiorDestinatario = 'codigoOrgaoSuperiorDestinatario'
c_orgaoSuperiorDestinatario = 'orgaoSuperiorDestinatario'
c_codigoOrgaoDestinatario = 'codigoOrgaoDestinatario'
c_orgaoDestinatario = 'orgaoDestinatario'
c_nomeFornecedor = 'nomeFornecedor'
c_cnpjFornecedor = 'cnpjFornecedor'
c_municipioFornecedor = 'municipioFornecedor'
c_chaveNotaFiscal = 'chaveNotaFiscal'
c_valorNotaFiscal = 'valorNotaFiscal'
c_tipoEventoMaisRecente = 'tipoEventoMaisRecente'
c_dataTipoEventoMaisRecente = 'dataTipoEventoMaisRecente'
c_dataEmissao = 'dataEmissao'
c_numero = 'numero'
c_serie = 'serie'

# convertendo dtype da coluna 'valorNotaFiscal' para float
base_dados[c_valorNotaFiscal] = base_dados[c_valorNotaFiscal].apply(lambda x: str(x).replace('.', '').replace(',', '.'))
base_dados[c_valorNotaFiscal] = base_dados[c_valorNotaFiscal].astype('float64')


print(base_dados.columns[c_nomeFornecedor])