#-------- contexto: Atividade 3 de Python - Dia 3 ---------

#03 Crie uma função chamada calcular_media(lista_de_notas) que receba uma lista de notas (números float) e retorne a média dessas notas.
# No programa principal:
# Peça ao usuário quantos alunos serão cadastrados.
# Para cada aluno, peça o nome e as 3 notas.
# Use a função para calcular a média e mostre o nome e a média.
# ➕ Bônus: diga se o aluno foi "Aprovado" (média >= 7) ou "Reprovado".

# def calcular_media(quantosAlunos):
#     alunos = []
#     mediasAlunos = []
    
#     for i in range(quantosAlunos):
#         nomesAlunos = input("nome do aluno: ")
#         n1 = int(input("nota 1 do aluno: "))
#         n2 = int(input("nota 2 do aluno: "))
#         n3 = int(input("nota 3 do aluno: "))
#         nF = (n1 + n2 + n3) / 3
#         mediasAlunos = f"nome: {nomesAlunos} nota: {nF}"
#         if nF >= 7:
#             print("Aprovado: ", mediasAlunos)
#         else:
#             print("Reprovado: ", mediasAlunos)
        
#         alunos.append({"nome": nomesAlunos, "media": nF})

#     ## desafio extra: mostrar a média de todos os alunos 
#     print("\nBoletim dos alunos:")
#     for aluno in alunos:
#         print(f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}")

# quantosAlunos = int(input("Quantos alunos serão cadastrados? "))
# calcular_media(quantosAlunos)
