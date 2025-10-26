# pip install pandas nesessário caso não tenha a biblioteca instalada
# pip install matplotlib nesessário caso não tenha a biblioteca instalada


#-------- contexto: Atividade 1 de Python - Dia 4 ---------

## Você é novo analista das Lojas Americanas, e visto queda de venda em dias de chuva,
# de forma prever ações para reduzir perda de vendas em dias de chuva,
# faça um sistema em python que analise os dados da tabela disponibilizada entregue seguintes informações:
#   - Shape do arquivo
#   - Colunas existentes
#   - Informação (info) do arquivo
#   - Quantos dados nulos existe
#   - Qual correlação e resumo estatístico (describe)
#   - Gráfico histograma
#   - Gráfico com Linear Regression
#   - E uma forma de digitar o mm do próximo dia conforme previsão do tempo e mostre quanto está previsto para vender

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

n_linhas = 1000

chuva = np.random.exponential(scale=5, size=n_linhas)
chuva = np.clip(chuva, 0, 50)  # limita entre 0 e 50 mm

vendas = 5000 - (chuva * np.random.uniform(30, 70)) + np.random.normal(0, 200, n_linhas)
vendas = np.clip(vendas, 500, None)  # mínimo 500

df = pd.DataFrame({
    'ValorDaVendas': vendas.round(2),
    'MilimetrosChuva': chuva.round(2)
})

df.to_csv("vendas_chuva.csv", index=False)

print("--- Arquivo CSV gerado com sucesso! ---\n")
print(df.head())

print("\n--- Shape do DataFrame ---\n", df.shape)
print("\n--- Colunas do DataFrame ---\n", df.columns)
print("\n--- Informações do DataFrame ---\n")
print(df.info())
print("\n--- Dados nulos por coluna ---\n", df.isnull().sum())

print("\n--- Correlação ---\n", df.corr())
print("\n--- Resumo Estatístico (describe) ---\n", df.describe())

plt.figure(figsize=(10, 5))
plt.hist(df["MilimetrosChuva"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribuição da Chuva (mm)")
plt.xlabel("Milímetros de chuva")
plt.ylabel("Frequência")
plt.show()

X = df[['MilimetrosChuva']]
y = df['ValorDaVendas']

modelo = LinearRegression()
modelo.fit(X, y)

x_novo = np.linspace(0, 50, 100).reshape(-1, 1)
y_pred = modelo.predict(x_novo)

plt.figure(figsize=(10, 5))
plt.scatter(df['MilimetrosChuva'], df['ValorDaVendas'], color='purple', alpha=0.5, label='Dados Reais')
plt.plot(x_novo, y_pred, color='red', linewidth=2, label='Regressão Linear')
plt.title("Relação entre Chuva e Vendas")
plt.xlabel("Milímetros de Chuva")
plt.ylabel("Valor das Vendas")
plt.legend()
plt.show()

mm_proximo_dia = float(input("\nDigite a previsão de chuva (mm) para o próximo dia: "))
previsao_venda = modelo.predict([[mm_proximo_dia]])
print(f"\n💧 Com {mm_proximo_dia:.2f} mm de chuva, está previsto vender aproximadamente R$ {previsao_venda[0]:.2f}")
