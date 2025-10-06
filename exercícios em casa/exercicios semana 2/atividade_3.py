#-------- contexto: Exercício 3 de Python ---------

## ATIVIDADE 3
# Receber as notas de 10 alunos em uma disciplina, calcular a média geral,
# contar quantos alunos ficaram acima ou abaixo da média e mostrar um gráfico de distribuição das notas.
# Estruturas usadas: Laços de repetição (for), estrutura de condição (if/else), vetor/array, gráficos.

# Passos:
# 1. O programa deve receber 10 notas dos alunos.
# 2. Calcular a média geral.
# 3. Contar quantos alunos ficaram acima e quantos abaixo da média.
# 4. Mostrar um gráfico de distribuição das notas.

import matplotlib.pyplot as plt

notasAlunos = []

for i in range(1, 11): 
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno número {i}: "))
            if 0 <= nota <= 10:
                notasAlunos.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

mediaGeral = sum(notasAlunos) / len(notasAlunos)
acima_media = sum(1 for n in notasAlunos if n > mediaGeral)
abaixo_media = sum(1 for n in notasAlunos if n < mediaGeral)

print("\n--- Resultados ---")
print(f"Média geral da turma: {mediaGeral:.2f}")
print(f"Alunos acima da média: {acima_media}")
print(f"Alunos abaixo da média: {abaixo_media}")

plt.figure(figsize=(8,5))
plt.bar(range(1, 11), notasAlunos, color='skyblue', label='Notas dos alunos')
plt.axhline(y=mediaGeral, color='red', linestyle='--', label='Média geral')
plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.title("Distribuição das notas dos alunos")
plt.legend()
plt.show()
