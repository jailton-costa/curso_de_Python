#-------- contexto: Atividade 3 de Python - Dia 1 ---------

# faça um progarama de loja de contruçao civil, onde peça o nome do cliente, nome do vendedor,
# o nome do produto, o valor do produto. no fim mostre:
# nome do cliente e o valor que ele pagou dando 20% de desconto,
# e também mostre o valor do vendendor e que ele ganhou de comisao no produto,
# sendo que o vendedor ganha 4% de comiçao.

print("olá, cliente tudo bem! responda as informações abaixo:")

nome = input("Qual é o seu nome ?")

nomeV = input("Qual é o nome do vendedor ?")

produto = input("Qual é o nome do produto ?")

valor = float(input("Qual é o valor do produto ?"))

desconto = valor * 0.2

comissao = valor * 0.04

valorFinal = valor - desconto

valorVendedor = comissao

print("o cliente: ",nome," comprou o produto: ",produto," e pagou com 20% de desconto o valor de: ",valorFinal)

print("o vendedor: ",nomeV," ganhou de comiçao o valor de: ",valorVendedor)

print("fim do programa, volte sempre!")