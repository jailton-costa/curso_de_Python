#-------- contexto: Exercício 10 de Python ---------

# Programa que pede nome e idade de 3 pessoas
# Mostra a média das idades e a maior idade

idades = []  # lista para guardar as idades
nomes = []   # lista para guardar os nomes

for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

media_idade = sum(idades) / 3
maior_idade = max(idades)

print(f"\nA média de idade é {media_idade:.2f}")
print(f"A maior idade entre eles é {maior_idade}")
print("Fim do programa de cálculo de idades.")