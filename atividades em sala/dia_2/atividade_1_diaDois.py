# Você trabalha no setor de logística de uma empresa de varejo. Sua função é acompanhar as entradas de produtos no estoque durante o mês.
# Use um laço while para permitir o cadastro de produtos (nome do produto) até que o usuário digite "sair".
# Para cada produto, use um laço for para pedir a quantidade recebida por semana (4 semanas no total).
# Calcule e mostre:
# A média semanal de entrada de cada produto.
# O total geral de produtos recebidos no mês.
# Exiba dois gráficos com matplotlib:
# 📈 Gráfico de linha mostrando o total de produtos recebidos por semana (somando todos os produtos).
# 📊 Gráfico de barras mostrando o total mensal recebido por produto.
import matplotlib.pyplot as plt

listaProdutos = []
listaTotaisMensais = []
totalGeralMensal = 0
continuar = 's'

while continuar.lower() in ['s', 'sim']:
    nomeProduto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()
    if nomeProduto.lower() == 'sair':
        break
    
    totalMensal = 0
    for semana in range(1, 5):
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade recebida na semana {semana} para {nomeProduto}: "))
                break
            except ValueError:
                print("⚠️ Entrada inválida! Digite um número inteiro.")
        totalMensal += quantidade
    
    mediaSemanal = totalMensal / 4
    print(f"Média semanal de entrada para {nomeProduto}: {mediaSemanal:.2f}")
    
    listaProdutos.append(nomeProduto)
    listaTotaisMensais.append(totalMensal)
    totalGeralMensal += totalMensal
    
    continuar = input("Deseja adicionar outro produto? (s/n): ")

print(f"\nTotal geral de produtos recebidos no mês: {totalGeralMensal}")

semanas = [1, 2, 3, 4]
totaisSemanais = [0, 0, 0, 0]

for i in range(len(listaProdutos)):
    for semana in range(4):
        totaisSemanais[semana] += listaTotaisMensais[i] / 4

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(semanas, totaisSemanais, marker='o', color='purple')
plt.title('Total de Produtos Recebidos por Semana')
plt.xlabel('Semana')
plt.ylabel('Total de Produtos')
plt.xticks(semanas)

plt.subplot(1, 2, 2)
plt.bar(listaProdutos, listaTotaisMensais, color='skyblue')
plt.title('Total Mensal Recebido por Produto')
plt.xlabel('Produto')
plt.ylabel('Total Mensal')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()