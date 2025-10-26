#-------- contexto: Exercício 4 de Python ---------

# ATIVIDADE 4
# Objetivo: Criar um sistema simples de controle de estoque de um
# supermercado. O programa deve perguntar o nome e a quantidade de 5
# produtos no estoque, e depois mostrar se algum produto está abaixo do
# estoque mínimo (definido pelo usuário) e mostrar um gráfico com o estoque atual de cada produto.
# Estruturas usadas: Laços de repetição (for), estrutura de condição (if/else), vetor/array, gráficos.

# Passos:
# 1. Perguntar o nome e a quantidade de 5 produtos.
# 2. Perguntar o estoque mínimo.
# 3. Verificar se algum produto está abaixo do estoque mínimo e imprimir um alerta.
# 4. Plotar um gráfico de barras com o estoque de cada produto.

import matplotlib.pyplot as plt

produtos = []
quantidades = []

print("Cadastro de produtos (5 itens):")
for i in range(1, 6):
    nome = input(f"Nome do produto {i}: ")
    while True:
        try:
            quantidade = int(input(f"Quantidade em estoque de {nome}: "))
            break
        except ValueError:
            print("Digite um número inteiro válido.")
    produtos.append(nome)
    quantidades.append(quantidade)

while True:
    try:
        estoque_minimo = int(input("Digite o estoque mínimo permitido: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print("\n--- Verificação de Estoque ---")
for nome, qtd in zip(produtos, quantidades):
    if qtd < estoque_minimo:
        print(f"ALERTA: {nome} está abaixo do estoque mínimo! (Qtd: {qtd})")
    else:
        print(f"{nome} está dentro do estoque. (Qtd: {qtd})")

plt.figure(figsize=(8,5))
plt.bar(produtos, quantidades, color='skyblue')
plt.axhline(y=estoque_minimo, color='red', linestyle='--', label='Estoque Mínimo')
plt.xlabel("Produtos")
plt.ylabel("Quantidade em Estoque")
plt.title("Controle de Estoque do Supermercado")
plt.legend()
plt.show()
