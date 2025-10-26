# Você é programador da loja de departamento Americanas.
# Faça um programa que peça para incluir nome de vendedores até quantidade que o usuário não quiser mais.
# Após isso, o programa deve habilitar solicitação da venda do mês de Março dos vendedores.
# Com Isso, você deve tirar a média do mês de Março, sendo que deve ter um gráfico mostrando resultado do mês Janeiro(Vendeu 50mil) e Fevereiro(vendeu 30mil), obviamente informando também Março no gráfico.
# Por fim mostrar em outro gráfico vendas por vendedor.
import matplotlib.pyplot as plt
listaVendedores = []
listaVendas = []
totalVendas = 0
continuar = 's'

while continuar.lower() == 's':
    nome = input("Digite o nome do vendedor: ").strip()
    venda = float(input(f"Digite o valor das vendas de {nome} em março: "))
    listaVendedores.append(nome)
    listaVendas.append(venda)
    totalVendas += venda
    continuar = input("Deseja adicionar outro vendedor? (s/n): ")
    mediaVendas = totalVendas / len(listaVendedores) if listaVendedores else 0
print(f"Média de vendas em março: R$ {mediaVendas:.2f}")

meses = ['Janeiro', 'Fevereiro', 'Março']
vendasMeses = [500000, 30000, totalVendas]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(meses, vendasMeses, color=['blue', 'orange', 'green'])
plt.title('Vendas por Mês')
plt.ylabel('Vendas (R$)')
plt.subplot(1, 2, 2)
plt.bar(listaVendedores, listaVendas, color='purple')
plt.title('Vendas por Vendedor em Março')
plt.ylabel('Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()