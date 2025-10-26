#-------- contexto: Exercicio 6 de Python ---------

# 6) Elaborar um programa que alerte sobre os riscos de animais em
# extinção. O usuário deve digitar o nome da espécie e a sua população
# (total de indivíduos). Populações entre 0 e 500 indivíduos, são
# classificadas como "Espécie criticamente em perigo";, populações entre
# 501 e 1000 indivíduos, são classificadas como; "Espécie em perigo"; e
# populações entre 1001 e 5000 indivíduos, são classificadas como
# "Espécie vulnerável!";

print("Olá, responda as informações abaixo:")
nome_especie = input("Qual é o nome da espécie ?")
populacao = int(input("Qual é a população (total de indivíduos) dessa espécie ?"))
if 0 <= populacao <= 500:
    print(f"A espécie {nome_especie} está classificada como: Espécie criticamente em perigo.")
elif 501 <= populacao <= 1000:
    print(f"A espécie {nome_especie} está classificada como: Espécie em perigo.")
elif 1001 <= populacao <= 5000:
    print(f"A espécie {nome_especie} está classificada como: Espécie vulnerável.")
else:
    print(f"A espécie {nome_especie} não está em risco de extinção.")
print("fim do programa, fique bem!")