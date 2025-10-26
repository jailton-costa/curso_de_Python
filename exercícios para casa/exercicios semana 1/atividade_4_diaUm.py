#-------- contexto: Exercício 4 de Python ---------

#4) Fazer um programa no qual o usuário digite a sua altura e o seu peso,
# ao final mostre o IMC (índice de massa corporal) e uma mensagem se está
# abaixo do peso (IMC menor que 18), na faixa de peso ideal (IMC de 18 a
# 25) ou acima do peso (IMC maior 25). IMC = peso / (altura * altura).

print("Olá, responda as informações abaixo:")
altura = float(input("Qual é a sua altura em metros ?"))
peso = float(input("Qual é o seu peso em kg ?"))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")
if imc < 18:
    print("Você está abaixo do peso.")

elif 18 <= imc <= 25:
    print("Você está na faixa de peso ideal.")

else:
    print("Você está acima do peso.")
print("fim do programa imc")