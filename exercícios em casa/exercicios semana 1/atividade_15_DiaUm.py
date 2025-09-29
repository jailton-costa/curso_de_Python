#------ contexto: Exercício 15 de Python ---------

# 15) Classificação de alunos por nota

nota = float(input("Digite a nota do aluno (0 a 100): "))

if 90 <= nota <= 100:
    conceito = "A (Excelente)"
elif 80 <= nota <= 89:
    conceito = "B (Bom)"
elif 70 <= nota <= 79:
    conceito = "C (Regular)"
elif 60 <= nota <= 69:
    conceito = "D (Passou)"
else:
    conceito = "F (Reprovado)"

print(f"O aluno recebeu: {conceito}")
print("Fim do programa de classificação de alunos.")