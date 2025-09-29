#-------- contexto: Exercicio 21 de Python ---------

import random

opcoes = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(opcoes)
usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

print(f"PC escolheu: {pc}")

if usuario == pc:
    resultado = "Empate"
elif (usuario == "Pedra" and pc == "Tesoura") or \
     (usuario == "Papel" and pc == "Pedra") or \
     (usuario == "Tesoura" and pc == "Papel"):
    resultado = "Você venceu!"
else:
    resultado = "Você perdeu!"

print(resultado)
print("Fim do jogo, obrigado por jogar!")