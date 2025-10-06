#-------- contexto: Exercício 5 de Python ---------

# ATIVIDADE 5
# O programa deve receber o valor dos gastos diários durante uma semana e
# calcular o total gasto, a média diária de gastos e quantos dias ficaram acima da
# média. O programa também deve gerar um gráfico de pizza para representar a porcentagem de gasto por dia.
# Estruturas usadas: Laços de repetição (for), estrutura de condição (if/else), vetor/array, gráficos.

# Passos:
# 1. O programa deve receber os valores dos gastos durante 7 dias.
# 2. Calcular o total gasto e a média diária.
# 3. Contar quantos dias os gastos foram acima da média.
# 4. Gerar um gráfico de pizza com os valores de cada dia.

import matplotlib.pyplot as plt
import numpy as np

gastos = []
print("Digite os gastos diários da semana (7 dias):")
for dia in range(1, 8):
    while True:
        try:
            valor = float(input(f"Dia {dia}: R$ "))
            gastos.append(valor)
            break
        except ValueError:
            print("Digite um valor numérico válido.")

total_gasto = sum(gastos)
media_gasto = np.mean(gastos)
dias_acima_media = sum(1 for g in gastos if g > media_gasto)

print("\n--- Resultados ---")
print(f"Total gasto na semana: R$ {total_gasto:.2f}")
print(f"Média diária de gastos: R$ {media_gasto:.2f}")
print(f"Dias com gastos acima da média: {dias_acima_media}")

dias = [f"Dia {i}" for i in range(1, 8)]
cores = plt.cm.tab20.colors  # cores variadas
plt.figure(figsize=(7,7))
plt.pie(gastos, labels=dias, autopct="%1.1f%%", colors=cores)
plt.title("Porcentagem de gastos diários")
plt.show()
