#-------- contexto: Exercicio 8 de Python ---------

# Programa que pede dois números e mostra quem é maior ou se são iguais

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print(f"{n1} é igual a {n2}")
print("Fim do programa de comparação.")