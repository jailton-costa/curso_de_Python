#------ contexto: Atividade 2 de Python - Dia 1 ---------

#faça um programa para uma nutricionista que peça o nome do paciente, nacimento, peso e altura.
#no fim mostre a paciente: tal possui: tal anos de idade com imc: tal

print("oii tudo bem, responda as informações abaixo:")

nome = input("Qual é o seu nome ?")

nascimento = int(input("Qual é o seu ano de nascimento ?"))

peso = int(input("Qual é o seu peso ?"))

altura = float(input("Qual é a sua altura ?"))

idade = 2025 - nascimento

imc = peso / (altura * altura)

print("o paciente: ",nome," possui ",idade," anos de idade com imc: ",imc)

print("fim do programa, fique bem!")