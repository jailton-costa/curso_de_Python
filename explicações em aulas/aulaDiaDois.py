# Aula 2 de Python 📘
# Conteúdo:
# - [x] `for`, `while`, `range`
# - [x] `if`, `else`, `elif`
# - [x] listas e `.append()`
# - [x] validação de entrada
# - [x] gráficos com matplotlib



# lista = ("p1","p2","p3")
# print(lista[1])
# # Programa simples em Python que interage com o usuário

# lista = input("Qual é o seu nome? ")
# num = int(input('Qual posição você quer ver?'))
# print(lista[num])
# lista.append("p5")
# print("lista toda: ", lista)



# repetição com while
# while = até 10
# x = 0
# while x < 10:
#     print("O valor de x é: ", x)
#     print("Dentro do while")
#     x += 1  #( 'x += 1' facil de usar ) = ( 'x = x + 1' difisil de usar )
# else:
#     print("Acabou, Fora do while")
# print("numero x = ",x)



#programa que peça se tem sol ou nublado ou chuvoso
# sol, mostre: pegue o protetor solar
# nublado, mostre: pegue um casaco
# chuvoso, mostre: pegue um guarda chuva
# nenhum dos três, mostre: opção inválida
# tempo = input("Como está o tempo hoje? (sol, nublado, chuvoso) ")
# while tempo != "sol" and tempo != "nublado" and tempo != "chuvoso":
#     print("Opção inválida, por favor responda novamente.")
#     tempo = input("Como está o tempo hoje? (sol, nublado, chuvoso) ")
    
# if tempo == "sol":
#     print("pegue o protetor solar")
#     print("fim do codigo")
    
# elif tempo == "nublado":
#     print("pegue um casaco")
#     print("fim do codigo")
    
# elif tempo == "chuvoso":
#     print("pegue um guarda chuva")
#     print("fim do codigo")
    
# else:
#     print("opção inválida")
#     print("fim do programa, fique bem!")



# aprendendo range
# for x in range(1, 10, 2): #começa em 1, vai até 10, de 2 em 2.
# for j in range(1, 5, 1): 
#     print("O valor de j é: ", j)
# for i in range(2, 10, 2):
#     print("O valor de i é: ", i)
# for s in range(1000, 0, -1): #contagem regressiva de 1000 até 1
#     print("O valor de s é: ", s)

# aprendendo range com listas
# fruta1 = input("Digite o nome de uma fruta: ")
# fruta2 = input("Digite o nome de outra fruta: ")
# fruta3 = input("Digite o nome de mais uma fruta: ")
# lista_frutas = [fruta1, fruta2, fruta3]
# for F in range(0,3,1):
#     print("Frutas: ", F)
# print("Fim do programa")


# aprendendo range com listas e append e break
# listaFruta = []

# for i in range(0,3,1):
#     fruta = input("Digite o nome de uma fruta: ")
#     listaFruta.append(fruta)
#     print("Fruta digitada é: ", listaFruta)
    
# for f in range(0,3,1):
#     print("essa fruta é ",listaFruta[f])
#     break

# print("todas as frutas: ", listaFruta)
# print("Fim do programa")



#contagem regressiva que vc escolhe o número inicial
# numero = int(input('Qual é o número inicial da contagem regressiva? (numero inteiro positivo) '))
# for s in range(numero, 0, -1): 
#     print("Contagem regreesiva em: ", s)
# print("Fim do programa")


# mostrando números ímpares de 0 a 100
# for f in range(0,101,1):
#     if( f % 2 != 0 ):
#         print(f, 'é ímpar')
# print("Fim da contagem")



# programa que pergunta se quer continuar
# resposta = input("Deseja continuar? ").strip().lower()

# if resposta in ["sim", "s", "yes", "y", "claro", "ok"]:
#     print("Você confirmou.")
# else:
#     print("Você negou.")


# vc tem, as vendas de um vendedor durante 12 meses, a meta mensal e 10.000, pra cada mes,
# informe se a meta foi alcansada e, no final mostre quantos meses foi batido os quais os meses.
# listaVendas = []
# metaMensal = 10000
# mesesBatidos = 0

# for v in range(1, 13):
#     venda = float(input(f"Digite o valor das vendas do mês {v}: "))
#     listaVendas.append(venda)
    
#     if venda >= metaMensal:
#         print(f"Parabéns! No mês {v}, você alcançou a meta de {metaMensal}.")
#         mesesBatidos += 1
        
#     else:
#         print(f"No mês {v}, você não alcançou a meta de {metaMensal}.")
        
# print(f"Você alcançou a meta em {mesesBatidos} meses.")
# print("Lista de vendas mensais: ", "mês1",listaVendas[0], " mês2",listaVendas[1], " mês3",listaVendas[2], " mês4",listaVendas[3], ' mês5',listaVendas[4], " mês6",listaVendas[5], " mês7",listaVendas[6], " mês8",listaVendas[7], " mês9",listaVendas[8], " mês10",listaVendas[9], " mês11",listaVendas[10], " mês12",listaVendas[11])
# print("Fim das vendas do ano, é do programa")



# fazendo um gráfico simples
# import matplotlib.pyplot as plt  # ' pip install matplotlib ' para funcionar
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.bar(x, y)
# plt.show()

# import random
# import numpy as np
# from matplotlib import pyplot as plt

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# plt.ion()         # Ativa modo interativo
# plt.plot(x, y)    
# plt.pause(1)
# plt.cla()         # Limpa o gráfico
# plt.pause(4)

# y = np.random.randint(10, 20, 10)  # Agora com 10 valores
# plt.bar(x, y)
# plt.pause(4)
# plt.ioff()        # Desativa modo interativo




# Você é programador da loja de departamento Americanas.
# Faça um programa que peça para incluir nome de vendedores até quantidade que o usuário não quiser mais.
# Após isso, o programa deve habilitar solicitação da venda do mês de Março dos vendedores.
# Com Isso, você deve tirar a média do mês de Março, sendo que deve ter um gráfico mostrando resultado do mês Janeiro(Vendeu 50mil) e Fevereiro(vendeu 30mil), obviamente informando também Março no gráfico.
# Por fim mostrar em outro gráfico vendas por vendedor.
# import matplotlib.pyplot as plt
# listaVendedores = []
# listaVendas = []
# totalVendas = 0
# continuar = 's'

# while continuar.lower() == 's':
#     nome = input("Digite o nome do vendedor: ").strip()
#     venda = float(input(f"Digite o valor das vendas de {nome} em março: "))
#     listaVendedores.append(nome)
#     listaVendas.append(venda)
#     totalVendas += venda
#     continuar = input("Deseja adicionar outro vendedor? (s/n): ")
#     mediaVendas = totalVendas / len(listaVendedores) if listaVendedores else 0
# print(f"Média de vendas em março: R$ {mediaVendas:.2f}")

# meses = ['Janeiro', 'Fevereiro', 'Março']
# vendasMeses = [500000, 30000, totalVendas]

# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.bar(meses, vendasMeses, color=['blue', 'orange', 'green'])
# plt.title('Vendas por Mês')
# plt.ylabel('Vendas (R$)')
# plt.subplot(1, 2, 2)
# plt.bar(listaVendedores, listaVendas, color='purple')
# plt.title('Vendas por Vendedor em Março')
# plt.ylabel('Vendas (R$)')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()




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

while continuar.lower() == 's' or continuar.lower() == 'sim':
    nomeProduto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()
    if nomeProduto.lower() == 'sair':
        break
    totalMensal = 0
    for semana in range(1, 5):
        quantidade = int(input(f"Digite a quantidade recebida na semana {semana} para {nomeProduto}: "))
        totalMensal += quantidade
        mediaSemanal = totalMensal / 4
    print(f"Média semanal de entrada para {nomeProduto}: {mediaSemanal:.2f}")
    listaProdutos.append(nomeProduto)
    listaTotaisMensais.append(totalMensal)
    totalGeralMensal += totalMensal
    continuar = input("Deseja adicionar outro produto? (s/n): ")
print(f"Total geral de produtos recebidos no mês: {totalGeralMensal}")
# Gráfico de linha para total semanal (somando todos os produtos)
semanas = [1, 2, 3, 4]
totaisSemanais = [0, 0, 0, 0]
for i in range(len(listaProdutos)):
    for semana in range(4):
        totaisSemanais[semana] += listaTotaisMensais[i] / 4  # Distribuindo igualmente para simplificação
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(semanas, totaisSemanais, marker='o')
plt.title('Total de Produtos Recebidos por Semana')
plt.xlabel('Semana')
plt.ylabel('Total de Produtos')
plt.xticks(semanas)
# Gráfico de barras para total mensal por produto
plt.subplot(1, 2, 2)
plt.bar(listaProdutos, listaTotaisMensais, color='skyblue')
plt.title('Total Mensal Recebido por Produto')
plt.xlabel('Produto')
plt.ylabel('Total Mensal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()   #------- codigo com erro cuidado !!! -------

# coresação do código de acima, codigo do professor, código corrigido
# import matplotlib.pyplot as plt
# nomes_produtos = []
# totais_produtos = []
# total_por_semana = [0, 0, 0, 0]
# total_geral = 0

# while True:
#     nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
#     if nome.lower() == "sair":
#         break

#     soma = 0
#     for i in range(4):
#         qtd = int(input(f"Quantidade da semana {i+1} para '{nome}': "))
#         soma += qtd
#         total_por_semana[i] += qtd
#         total_geral += qtd

#     media = soma / 4
#     print(f"Média semanal de '{nome}': {media:.2f} unidades\n")

#     nomes_produtos.append(nome)
#     totais_produtos.append(soma)  

# print(f"\nTotal geral de produtos recebidos no mês: {total_geral} unidades\n")

# # Gráfico 1: Linha - Total por semana
# plt.plot(["Semana 1", "Semana 2", "Semana 3", "Semana 4"], total_por_semana, marker='o')
# plt.title("?? Total por Semana")
# plt.xlabel("Semana")
# plt.ylabel("Quantidade")
# plt.grid(True)
# plt.show()

# # Gráfico 2: Barras - Total por produto
# plt.bar(nomes_produtos, totais_produtos, color='green')
# plt.title("?? Total por Produto no Mês")
# plt.xlabel("Produto")
# plt.ylabel("Quantidade")
# plt.show()