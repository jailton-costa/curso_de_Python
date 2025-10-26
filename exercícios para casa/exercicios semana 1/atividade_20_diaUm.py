#-------- contexto: Exercicio 20 de Python ---------

import re

senha = input("Digite sua senha: ")

if len(senha) < 8:
    nivel = "Fraca"
elif (re.search("[A-Z]", senha) and re.search("[a-z]", senha) 
      and re.search("[0-9]", senha) and re.search("[!@#$%^&*()_+=-]", senha)):
    nivel = "Forte"
else:
    nivel = "Média"

print(f"A senha é: {nivel}")
print("Fim do programa de análise de senha.")