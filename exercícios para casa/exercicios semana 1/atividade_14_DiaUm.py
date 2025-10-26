#------ contexto: Exercícios 14 de Python ------

# 14) Pontuação de peteca e classificação

# Entrada das 3 jogadas
pontuacoes = []
for i in range(1, 4):
    ponto = int(input(f"Digite a pontuação do arremesso {i} (0 a 5): "))
    pontuacoes.append(ponto)

total = sum(pontuacoes)

# Classificação
if total == 15:
    classificacao = "Deus da peteca"
elif 10 <= total <= 14:
    classificacao = "Petequeiro profissa"
elif 5 <= total <= 9:
    classificacao = "Petequeiro de final de semana"
elif 1 <= total <= 4:
    classificacao = "Pseudo-petequeiro"
else:
    classificacao = "Nunca petequeiro"

print(f"Pontuação total: {total}")
print(f"Classificação: {classificacao}")
print("Fim do programa de peteca, volte sempre!")