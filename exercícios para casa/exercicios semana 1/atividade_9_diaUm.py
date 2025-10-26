#-------- contexto: Exercício 9 de Python ---------

# Programa que verifica se um número é par ou ímpar e positivo ou negativo

n = int(input("Digite um número: "))

# Verificando par ou ímpar
if n % 2 == 0:
    print("O número é Par")
else:
    print("O número é Ímpar")

# Verificando positivo ou negativo
if n >= 0:
    print("O número é Positivo")
else:
    print("O número é Negativo")
print("Fim do programa, fique bem!")