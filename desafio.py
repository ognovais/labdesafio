import pandas as pd
import numpy as np
import datetime

def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    df.columns = df.columns.str.strip()
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d').dt.date
    df['Quantidade Vendida'] = pd.to_numeric(df['Quantidade Vendida'], errors='coerce')
    df['Preço Unitário'] = pd.to_numeric(df['Preço Unitário'], errors='coerce')
    df['Valor Total'] = pd.to_numeric(df['Valor Total'], errors='coerce')
    return df

dados = carregar_dados('vendas.csv')

datas = np.array(dados['Data'])
quantidades = np.array(dados['Quantidade Vendida'])
precos = np.array(dados['Preço Unitário'])
valores_totais = np.array(dados['Valor Total'])
regioes = np.array(dados['Região'])
produtos = np.array(dados['Produto'])

media_valor_total = np.mean(valores_totais)
mediana_valor_total = np.median(valores_totais)
desvio_padrao_valor_total = np.std(valores_totais)

indice_maior_quantidade = np.argmax(quantidades)
produto_maior_quantidade = produtos[indice_maior_quantidade]

indice_maior_valor_total = np.argmax(valores_totais)
produto_maior_valor_total = produtos[indice_maior_valor_total]

valor_total_por_regiao = {regiao: np.sum(valores_totais[regioes == regiao]) for regiao in np.unique(regioes)}

vendas_por_dia = {str(data): np.sum(valores_totais[datas == data]) for data in np.unique(datas)}
venda_media_por_dia = np.mean(list(vendas_por_dia.values()))

dias_da_semana = np.array([data.weekday() for data in datas])
dia_com_mais_vendas = np.argmax([np.sum(dias_da_semana == dia) for dia in range(7)])

vendas_diarias = [np.sum(valores_totais[datas == data]) for data in np.unique(datas)]
variacao_diaria = np.diff(vendas_diarias)

print(f'Média do Valor Total das Vendas: {media_valor_total:.2f}')
print(f'Mediana do Valor Total das Vendas: {mediana_valor_total:.2f}')
print(f'Desvio Padrão do Valor Total das Vendas: {desvio_padrao_valor_total:.2f}')
print(f'Produto com maior quantidade vendida: {produto_maior_quantidade}')
print(f'Produto com maior valor total de vendas: {produto_maior_valor_total}')
print(f'Valor total de vendas por região: {valor_total_por_regiao}')
print(f'Venda média por dia: {venda_media_por_dia:.2f}')
print(f'Dia da semana com mais vendas (0=Segunda, 6=Domingo): {dia_com_mais_vendas}')
print(f'Variação diária no valor total de vendas: {variacao_diaria}')
