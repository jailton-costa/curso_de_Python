#-------- contexto: Exercício 16 de Python ---------

import random

# 16) Jogo de Par ou Ímpar
numero_pc = random.randint(1, 10)
escolha_usuario = input("Adivinhe se o número é Par ou Ímpar (P/I): ").upper()

resultado = "P" if numero_pc % 2 == 0 else "I"

print(f"O número sorteado foi {numero_pc}")
if escolha_usuario == resultado:
    print("Você acertou!")
else:
    print("Você errou!")
print("Fim do programa, fique bem!")