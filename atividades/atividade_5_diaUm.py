#-------- contexto: Atividade 5 de Python - Dia 1 ---------

# Avaliador de Média Escolar
# Descrição: Crie um programa que solicite ao usuário as notas de 3 provas de um aluno (de 0 a 10).
# O programa deve calcular a média e, com base nela, exibir o status do aluno.
# Aprovado: Média igual ou superior a 7.
# Recuperação: Média entre 5 e 6.9.
# Reprovado: Média abaixo de 5.
# Dica: Use if, elif e else para criar a lógica de avaliação.
# Exemplo de Saída:
# Notas 8, 7, 9: A média é 8.0. O aluno está Aprovado.
# Notas 5, 6, 6: A média é 5.6. O aluno está em Recuperação.
# Notas 4, 3, 2: A média é 3.0. O aluno está Reprovado.

print("Bem-vindo ao media escolar!")
print("digite as 3 notas de 3 provas:")

nota1 = int(input("Digite sua  primeira nota: "))
nota2 = int(input("Digite sua  segunda nota: "))
nota3 = int(input("Digite sua  terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7: print("Esse aluno esta Aprovado ( nota:", media,")")

elif media >= 5 and media < 7: print("Esse aluno esta Recuperação. ( nota:", media,")")

else: print("Esse aluno esta Reprovado. ( nota:", media,")")