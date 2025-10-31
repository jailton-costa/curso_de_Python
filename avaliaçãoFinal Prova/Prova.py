# # Avaliação objetiva - Prova
# professor: wuesley vargas de andrade
# curso: curso de python
# nome: jailton costa pereira
# data: 28/10/2025
# github: https://github.com/jailton-costa/curso_de_Python



# 1. Variáveis e entrada de dados
# Enunciado:
# Crie um programa que peça ao usuário seu nome e idade e exiba a seguinte mensagem:
# “Olá, [nome]! Você tem [idade] anos.”

print(("\n\n____Questão.1____\n"))
nomeVc = input("Digite seu nome: ")
idadeVc = int(input("Digite sua idade: "))

print(f"Olá, {nomeVc}! Você tem {idadeVc} anos.")




# 2. Operações matemáticas simples
# Enunciado:
# Peça dois números inteiros ao usuário e mostre:
# A soma,
# A diferença,
# O produto,
# O quociente.
print(("\n\n____Questão 2____\n"))
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

soma = n1 + n2
diferenca = n1 - n2
produto = n1 * n2
quociente = n1 / n2

print(f"\n--- calculos feitos ---\n Soma: {soma}\n Diferença: {diferenca}\n Produto: {produto}\n Quociente: {quociente:.2f}")




# 3. Estrutura condicional simples
# Enunciado:
# Peça a idade do usuário e diga se ele é menor de idade, adulto (18 a 59) ou idoso (60+).
# Habilidade: Uso de if, elif, else.
print(("\n\n____Questão.3____\n"))
idadeUser = int(input("Digite sua idade: "))

if idadeUser < 18:
    print(f"Você é menor de idade ({idadeUser})")
elif idadeUser < 60:
    print(f"Você é adulto ({idadeUser})")
else:
    print(f"Você é idoso ({idadeUser})")




# 4. Estrutura de repetição for
# Enunciado:
# Escreva um programa que mostre a tabuada de um número informado pelo usuário (de 1 a 10).
# Habilidade: Laço for e multiplicação iterativa.
print(("\n\n____Questão.4____\n"))
n1 = int(input("Digite o primeiro número inteiro: "))

print(f"tabuada de {n1}")
print(f"\n --- calculos feitos ---\n")

for i in range(1, 11):
    resultado = n1 * i
    print(f"{n1} x {i} = {resultado}")




# 5. Estrutura de repetição while
# Enunciado:
# Peça números ao usuário até que ele digite 0, e então mostre a soma total desses números.
# Habilidade: Laço while e controle de loop.
print(("\n\n____Questão.5____\n"))
somaTotalNs = 0
while True:
    nS = int(input("Digite um número: (ou 0 para sair) "))
    if nS == 0:
        break
    somaTotalNs += nS
print(f"A soma total dos números digitados é: {somaTotalNs}")




# 6. Lista e média de valores
# Enunciado:
# Leia 5 notas de alunos, guardando em uma lista e mostre:
# As notas digitadas,
# A média da turma,
# Quantos alunos ficaram acima da média.
# Habilidade: Listas, for, if e cálculo de média.
print(("\n\n____Questão.6____\n"))
notasAlunosLegais = []

for i in range(5):
    nts = float(input(f"Digite a nota do aluno legal papai {i + 1}: "))
    notasAlunosLegais.append(nts)
mediaTurmaLegal = sum(notasAlunosLegais) / len(notasAlunosLegais)

print(f"\nAs notas dos alunos legais digitadas foram: {notasAlunosLegais}.\n A média da turma legal foi: {mediaTurmaLegal:.2f}")

LegalAcimaMedia = sum(1 for nt in notasAlunosLegais if nt > mediaTurmaLegal)

print(f"Quantidade de alunos muito legais acima da média: {LegalAcimaMedia}")




# 7 . Crie um programa que com Classe Aluno com atributos de nome, idade e valor mensalidade,
# sendo que deve ter como método calculo de média, onde ao chamar o método deve passar 3 notas e o
# return deve ser como informação de passou quando acima de 7 ou reprovado abaixo de 7.
# Crie 3 objetos da classe aluno para teste, chamando o método de média
print(("\n\n____Questão.7____\n"))
class Aluno:
    def __init__(self, nomeAlu, idadeAlu, valorMens):
        self.nomeAlu = nomeAlu
        self.idadeAlu = idadeAlu
        self.valorMens = valorMens

    def calculo_media(self, n1, n2, n3):
        media = (n1 + n2 + n3) / 3
        if media >= 7:
            return f"{self.nomeAlu} passou com média {media:.2f}"
        else:
            return f"{self.nomeAlu} reprovou com média {media:.2f}"
        
aluno1 = Aluno("Sertanejo", 20, 500)
aluno2 = Aluno("Bruno &", 18, 600)
aluno3 = Aluno("Marrone", 23, 550)

print(aluno1.calculo_media(8, 7.5, 9))
print(aluno2.calculo_media(6, 5.5, 7))
print(aluno3.calculo_media(4, 6, 5))




# 8. Leitura de dados e estatísticas com pandas
# Enunciado:
# Crie um DataFrame com os seguintes dados:
# Aluno Nota Idade
# Ana 8.5 20
# Bruno 6.0 22
# Carla 7.2 19
# Diego 9.0 23
# Mostre:
# A média das notas,
# O aluno com a maior nota,
# A idade média dos alunos.
# Habilidade: pandas.DataFrame, estatísticas simples.
print(("\n\n____Questão.8____\n"))
import pandas as pd

dadosAlunosManeiros = {
    "Alu": ["Ana", "Bruno", "Carla", "Diego"],
    "nt": [8.5, 6.0, 7.2, 9.0],
    "Idd": [20, 22, 19, 23]
}

df = pd.DataFrame(dadosAlunosManeiros)

print(f"Dados dos alunos: {df}")

media_notas = df["nt"].mean()
print(f"\n Média das notas: {media_notas:.2f}")

aluMaiorNota = df.loc[df["nt"].idxmax(), "Alu"]
print(f"Aluno com a maior nota: {aluMaiorNota}")

media_idd = df["Idd"].mean()
print(f"Idade média dos alunos: {media_idd:.1f}")




# 9. Geração de gráfico simples
# Enunciado:
# Usando o matplotlib, crie um gráfico de barras mostrando as notas dos alunos do exercício anterior.
# Habilidade: matplotlib.pyplot.bar, título e rótulos de eixos.
print(("\n\n____Questão.9____\n"))
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Alu": ["ana", "Bruno", "Marrone", "Diego"],
    "Nt": [8.5, 6.0, 7.2, 9.0],
}

df = pd.DataFrame(dados)

plt.bar(df["Alu"], df["Nt"], color='skyblue', edgecolor='black')
plt.title("Notas dos Alunos Legais e maneiros")
plt.xlabel("Alu")
plt.ylabel("Nt")
plt.ylim(0, 10)
plt.show()




# 10. Análise de dados e gráfico combinado
# Enunciado:
# Usando pandas e matplotlib, crie um programa que leia (ou crie) um conjunto de dados de vendas
# com as colunas:
# Produto | Quantidade | Receita
# Depois:
# Calcule a receita total,
# Mostre o produto mais vendido,
# Gere um gráfico de linhas mostrando a evolução das receitas.
# Habilidade: pandas, agrupamentos, e visualização com matplotlib.
print(("\n\n____Questão.10____\n"))
import pandas as pd
import matplotlib.pyplot as plt

vendas = {
    "Produto": ["Camiseta", "Caneca", "Boné", "Camiseta", "Caneca", "Boné"],
    "Quantidade": [10, 8, 5, 12, 9, 7],
    "Receita": [200, 160, 125, 240, 180, 175]
}

dfV = pd.DataFrame(vendas)

receitaTotal = dfV["Receita"].sum()
print(f" Receita total: R$ {receitaTotal:.2f}")

produtoMvendido = dfV.groupby("Produto")["Quantidade"].sum().idxmax()
print(f" Produto mais vendido: {produtoMvendido}")

receitasProProduto = dfV.groupby("Produto")["Receita"].sum()

plt.plot(receitasProProduto.index, receitasProProduto.values, marker='o', color='green')
plt.title("Evolução das Receitas por Produto")
plt.xlabel("Produto")
plt.ylabel("Receita (R$)")
plt.grid(True)
plt.show()
