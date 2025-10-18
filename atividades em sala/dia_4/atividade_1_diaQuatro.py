#-------- contexto: Atividade 1 de Python - Dia 4 ---------

# Você é novo analista das Lojas Americanas, e visto queda de venda em dias de chuvas,
# de forma prever ações para reduzir perda de vendas em dias de chuva,
# faça um sistema em python que analise os dados da tabela disponibilizada entregue seguintes informações:

# 	- Shape do arquivo
# 	- Colunas existentes
# 	- Informação (info) do arquivo
# 	- Quantos dados nulos existe
# 	- Qual correlação e resumo estatístico(descrive)
# 	- Gráfico histograma
# 	- Gráfico com Linear Regression
# 	- E uma forma de digitar o mm do próximo dia conforme previsão do tempo e mostre quanto está previsto para vender

import pandas as pd
import numpy as np


n_linhas = 1000


chuva = np.random.exponential(scale=5, size = n_linhas)
chuva = np.clip(chuva, 0, 50)


vendas = 5000 - (chuva * np.random.uniform(30, 70)) + np.random.normal(0, 200, n_linhas)
vendas = np.clip(vendas, 500, None)

df = pd.DataFrame({
    'ValorDaVendas': vendas.round(2),
    'MilimetrosChuva': chuva.round(2)
})


df.to_csv("vendas_chuva.csv", index=False)

print("--- Arquivo CSV gerado com sucesso! ---\n\n")
print(df.head(5))
print("\n\n --- Shape do DataFrame --- \n", df.shape)
print("\n\n --- Colunas do DataFrame --- \n", df.columns)
print("\n\n --- Informações do DataFrame --- \n", df.info())
print("\n\n --- Dados nulos por coluna --- \n", df.isnull().sum())
