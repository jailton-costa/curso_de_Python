#-------- contexto: Exercicio 18 de Python ---------

# 18) Calculadora de IMC com classificação OMS

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
elif 25 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc <= 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print(f"IMC: {imc:.2f} - Classificação: {classificacao}")
print("Fim do programa de cálculo de IMC.")