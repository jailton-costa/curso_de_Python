#------ contexto: Atividade 1 de Python - Dia 1 ------

#faça um programa que peça o nome do aluno, nome do professor e três notas.
#calcule a média do aluno e mostre uma mensagem com o nome do aluno, nome do professor e a média

print("olá, responda as informações abaixo:")

nome = input("Qual é o seu nome ?") 
nomeP = input("Qual é o nome do professor ?") 

nota1 = float(input("primeira nota ? "))
nota2 = float(input("segunda nota ? "))
nota3 = float(input("terceira nota ? "))

media = (nota1 + nota2 + nota3) / 3

print("o aluno: ",nome," na aula da professor: ", nomeP, " ficou com média: ", media, ".")



#------ contexto: Atividade 2 de Python - Dia 1 ---------

#faça um programa para uma nutricionista que peça o nome do paciente, nacimento, peso e altura.
#no fim mostre a paciente: tal possui: tal anos de idade com imc: tal

# print("oii tudo bem, responda as informações abaixo:")

# nome = input("Qual é o seu nome ?")

# nascimento = int(input("Qual é o seu ano de nascimento ?"))

# peso = int(input("Qual é o seu peso ?"))

# altura = float(input("Qual é a sua altura ?"))

# idade = 2025 - nascimento

# imc = peso / (altura * altura)

# print("o paciente: ",nome," possui ",idade," anos de idade com imc: ",imc)
# print("fim do programa, fique bem!")



#-------- contexto: Atividade 3 de Python - Dia 1 ---------

# faça um progarama de loja de contruçao civil, onde peça o nome do cliente, nome do vendedor,
# o nome do produto, o valor do produto. no fim mostre:
# nome do cliente e o valor que ele pagou dando 20% de desconto,
# e também mostre o valor do vendendor e que ele ganhou de comisao no produto,
# sendo que o vendedor ganha 4% de comiçao.

# print("olá, cliente tudo bem! responda as informações abaixo:")

# nome = input("Qual é o seu nome ?")

# nomeV = input("Qual é o nome do vendedor ?")

# produto = input("Qual é o nome do produto ?")

# valor = float(input("Qual é o valor do produto ?"))

# desconto = valor * 0.2

# comissao = valor * 0.04

# valorFinal = valor - desconto

# valorVendedor = comissao

# print("o cliente: ",nome," comprou o produto: ",produto," e pagou com 20% de desconto o valor de: ",valorFinal)

# print("o vendedor: ",nomeV," ganhou de comiçao o valor de: ",valorVendedor)

# print("fim do programa, volte sempre!")