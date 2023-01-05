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

print(base_dados[c_valorNotaFiscal])