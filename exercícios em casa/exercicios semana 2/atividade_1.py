#-------- contexto: Exercício 1 de Python ---------

# Você trabalha no setor de Business Intelligence (BI) de uma empresa de
# tecnologia. Sua tarefa é monitorar a produtividade dos funcionários durante o
# mês.
# Crie um programa em Python que:
# Use um laço while para permitir o cadastro de funcionários (nome e setor) até
# que o usuário decida parar (ex: digitando &quot;sair&quot;).
# Para cada funcionário cadastrado, use um laço for para registrar a quantidade
# de tarefas concluídas por semana durante o mês de Setembro (4 semanas).
# Calcule e mostre:
# A média de tarefas por funcionário no mês (len() pode ser usado para contar as
# semanas).
# O total geral de tarefas da equipe no mês.
# Exiba dois gráficos com matplotlib:
# Gráfico 1 (linha): mostra a evolução da produtividade da equipe nas 4
# semanas de Setembro (somando tarefas de todos os funcionários por semana).
# Gráfico 2 (barras): mostra a produtividade total por funcionário no mês de
# Setembro.

import matplotlib.pyplot as plt
funcionarios = []

while True:
    nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    setor = input("Digite o setor do funcionário: ")

    tarefas_semanais = []
    for semana in range(1, 5):
        while True:
            try:
                tarefas = int(input(f"Quantas tarefas {nome} concluiu na semana {semana}? "))
                if tarefas < 0:
                    print("Número inválido. Digite um valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
        tarefas_semanais.append(tarefas)

    funcionarios.append({
        "nome": nome,
        "setor": setor,
        "tarefas": tarefas_semanais
    })

total_geral = 0
media_por_funcionario = []
evolucao_semanal = [0, 0, 0, 0] 

for func in funcionarios:
    total_func = sum(func["tarefas"])
    media_func = total_func / len(func["tarefas"])
    media_por_funcionario.append((func["nome"], media_func))
    total_geral += total_func

    for i, t in enumerate(func["tarefas"]):
        evolucao_semanal[i] += t

print("\n=== Resultados ===")
for nome, media in media_por_funcionario:
    print(f"Média de tarefas de {nome} no mês: {media:.2f}")
print(f"Total geral de tarefas da equipe no mês: {total_geral}")

semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
plt.figure(figsize=(10,5))
plt.plot(semanas, evolucao_semanal, marker='o', color='blue', linestyle='-', linewidth=2)
plt.title("Evolução da produtividade da equipe - Setembro")
plt.xlabel("Semana")
plt.ylabel("Total de tarefas concluídas")
plt.grid(True)

nomes = [func["nome"] for func in funcionarios]
totais_func = [sum(func["tarefas"]) for func in funcionarios]

plt.figure(figsize=(10,5))
plt.bar(nomes, totais_func, color='green')
plt.title("Produtividade total por funcionário - Setembro")
plt.xlabel("Funcionário")
plt.ylabel("Total de tarefas")
plt.xticks(rotation=45)
plt.show()
print("Fim do programa de monitoramento de produtividade.")

# esse exercício é mesmo do mal passe um mal bucado !!!