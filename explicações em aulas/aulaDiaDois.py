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



# fazendo um gráfico simples é explicando matplotlib
import matplotlib.pyplot as plt  # ' pip install matplotlib ' para funcionar
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.bar(x, y)   # Cria um gráfico de barras com os valores de x e y
plt.show()      # Exibe o gráfico na tela

import random # gerar números aleatórios.
import numpy as np # manipulação de arrays (vetores e matrizes).
from matplotlib import pyplot as plt # criar gráficos.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.ion()        # Ativa o modo interativo do matplotlib (permite atualizar o gráfico sem travar o programa)
plt.plot(x, y)   # Plota uma linha conectando os pontos de x e y
plt.pause(1)     # Pausa 1 segundo para o gráfico aparecer
plt.cla()        # Limpa o gráfico atual, deixando a figura pronta para desenhar outro gráfico
plt.pause(4)     # Pausa 4 segundos antes de desenhar o próximo gráfico

y = np.random.randint(10, 20, 10)  # Gera 10 valores aleatórios entre 10 e 20
plt.bar(x, y)    # Cria um gráfico de barras com os novos valores aleatórios
plt.pause(4)     # Pausa 4 segundos para visualizar o gráfico
plt.ioff()       # Desativa o modo interativo, gráficos futuros precisarão de plt.show() para aparecer
plt.show()       # Exibe o gráfico final na tela