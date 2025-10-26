#-------- contexto: Exercício 2 de Python ---------

# ATIVIDADE 2
# Criar um programa que leia as temperaturas diárias de uma semana (7 dias) e calcule a média das temperaturas,
# além de verificar se algum dia foi mais quente ou mais frio que a média.
# O programa também deve mostrar um gráfico com as temperaturas diárias.

# Estruturas usadas: Laços de repetição (for ou while), estrutura de condição (if/else), vetor/array, gráficos.

# Passos:
# 1. O programa deve receber 7 entradas de temperatura para cada dia da semana.
# 2. Calcular a média das temperaturas.
# 3. Verificar quantos dias foram acima ou abaixo da média.
# 4. Plotar um gráfico de barras com as temperaturas diárias


import matplotlib.pyplot as plt

temperaturas = [] 
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

for dia in dias:
    temp = float(input(f"Digite a temperatura de {dia}: "))
    temperaturas.append(temp)

soma = 0
contador = 0
for t in temperaturas:
    soma += t
    contador += 1

media = soma / contador

acima = 0
abaixo = 0

for t in temperaturas:
    if t > media:
        acima += 1
    elif t < media:
        abaixo += 1

print(f"\nMédia da semana: {media:.2f}°C")
print(f"Dias acima da média: {acima}")
print(f"Dias abaixo da média: {abaixo}")

plt.bar(dias, temperaturas, color='skyblue')
plt.axhline(y=media, color='red', linestyle='--', label=f"Média ({media:.1f}°C)")
plt.title("Temperaturas da Semana")
plt.xlabel("Dias da Semana")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.show()