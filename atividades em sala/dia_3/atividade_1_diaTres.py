#-------- contexto: Atividade 1 de Python - Dia 3 ---------

# 01 Crie uma função chamada dobro(numero) que receba um número e retorne o dobro dele.
# No programa principal, peça ao usuário um número, chame a função e mostre o resultado na tela.

def dobro(numero):
    return numero * 2

num = float(input("Digite um número: "))
resultado = dobro(num)
print("O dobro de", num, "é:", resultado)