#-------- contexto: Exercício 6 de Python ---------

# ATIVIDADE 6
# Criar um sistema que leia o número de vendas diárias de um vendedor durante
# um mês (30 dias), calcule as metas atingidas, verifique quais dias superaram a
# média diária de vendas e gere gráficos para visualização do desempenho.
# O exercício envolve:
# Leitura e processamento de dados.
# Cálculo de média, desvio padrão e metas.
# Análise condicional de desempenho.
# Geração de gráficos.

# Passos:
# 1. Entrada de Dados:
# o O sistema deve receber, via input, o número de vendas diárias de
# um vendedor durante 30 dias.
# o O sistema deve também receber a meta de vendas diária (um
# valor fixo que o vendedor deve atingir todo dia).

# 2. Cálculos:
# o Calcule a média de vendas diárias.
# o Calcule o desvio padrão das vendas (para analisar a variação do
# desempenho).

# o Calcule quantos dias o vendedor superou a meta diária de
# vendas.

# 3. Análise de Resultados:
# o Verifique quantos dias o vendedor teve vendas acima da média e
# quantos dias ficaram abaixo da média.
# o Para cada dia que teve vendas acima da média, adicione um
# marcador especial indicando &quot;Desempenho acima da média&quot;.

# 4. Visualização:
# o Gere um gráfico de barras mostrando as vendas diárias do
# vendedor.
# o Gere um gráfico de linha representando a média de vendas
# diárias ao longo do mês.
# o Gere um gráfico de dispersão (scatter) mostrando a dispersão
# das vendas diárias em relação à meta de vendas.

# 5. Saída:
# o Exiba a média de vendas diárias e o desvio padrão.
# o Exiba o número de dias acima e abaixo da média.
# o Exiba o número de dias que o vendedor superou a meta.



import matplotlib.pyplot as plt
import numpy as np

vendas = []
print("Digite as vendas diárias do vendedor para 30 dias:")
for dia in range(1, 31):
    while True:
        try:
            venda = int(input(f"Dia {dia}: "))
            vendas.append(venda)
            break
        except ValueError:
            print("Digite um número inteiro válido.")

meta = int(input("Digite a meta diária de vendas: "))

media_vendas = np.mean(vendas)
desvio_padrao = np.std(vendas)

dias_acima_meta = sum(1 for v in vendas if v > meta)

dias_acima_media = sum(1 for v in vendas if v > media_vendas)
dias_abaixo_media = sum(1 for v in vendas if v < media_vendas)

marcadores = ["Desempenho acima da média" if v > media_vendas else "" for v in vendas]

print("\n--- Resultados ---")
print(f"Média de vendas diárias: {media_vendas:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Dias acima da média: {dias_acima_media}")
print(f"Dias abaixo da média: {dias_abaixo_media}")
print(f"Dias que superaram a meta: {dias_acima_meta}")

for i, marcador in enumerate(marcadores, start=1):
    if marcador:
        print(f"Dia {i}: {marcador}")

dias = list(range(1, 31))

plt.figure(figsize=(12, 5))
plt.bar(dias, vendas, color='skyblue', label='Vendas Diárias')
plt.axhline(y=media_vendas, color='r', linestyle='--', label='Média')
plt.axhline(y=meta, color='g', linestyle='--', label='Meta')
plt.xlabel("Dia")
plt.ylabel("Vendas")
plt.title("Vendas Diárias do Vendedor")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
plt.scatter(dias, vendas, color='purple', label='Vendas')
plt.axhline(y=meta, color='g', linestyle='--', label='Meta')
plt.axhline(y=media_vendas, color='r', linestyle='--', label='Média')
plt.xlabel("Dia")
plt.ylabel("Vendas")
plt.title("Dispersão das Vendas Diárias")
plt.legend()
plt.show()

# esse foi dificil para modificar a tabela :´>