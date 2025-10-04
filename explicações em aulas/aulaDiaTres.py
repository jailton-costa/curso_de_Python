# Aula 2 de Python 📘
# Conteúdo:
# - [x] Funções
# - [x] Parâmetros e Argumentos
# - [x] Retorno de Funções
# - [x] Funções com Múltiplos Parâmetros
# - [x] Funções Aninhadas
# - [x] Escopo de Variáveis
# - [x] Documentação de Funções


# nome = input("Qual é o seu nome? ")
# def nomeDeUser(nome):
#     print("Olá, " + nome + "! Seja bem-vindo(a) ao sistema.")
# nomeDeUser(nome)

# from datetime import datetime
# def hora_Agora():
#     hora_Agora = datetime.now().hour
#     hora_Agora2 = datetime.now().minute
#     print("Hora atual:", hora_Agora, ":", hora_Agora2)
# hora_Agora()


# def calculadora ():
#     escolha = input("Escolha uma operação (soma, subtração, multiplicação, divisão): ").strip().lower()
#     n1 = int(input("Digite um número: "))
#     n2 = int(input("Digite outro número: "))
#     if escolha == "soma":
#       nF = n1 + n2
#       print("A soma de", n1, "+", n2, "é igual a:", nF)
#     elif escolha == "subtração":
#         nF = n1 - n2
#         print("A subtração de", n1, "-", n2, "é igual a:", nF)
#     elif escolha == "multiplicação":
#         nF = n1 * n2
#         print("A multiplicação de", n1, "*", n2, "é igual a:", nF)
#     elif escolha == "divisão":
#         if n2 != 0:
#             nF = n1 / n2
#             print("A divisão de", n1, "/", n2, "é igual a:", nF)
#         else:
#             print("Erro: Divisão por zero não é permitida.")
#     else:
#         print("Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão.")
# calculadora()


# def parInpar():
#     numero = int(input("Digite um número inteiro: "))
#     if numero % 2 == 0:
#         print("O número", numero, "é par.")
#     else:
#         print("O número", numero, "é ímpar.")
# parInpar()


# def calcularArea(largura, comprimento):
#     area = largura * comprimento
#     return area

# larguraLocal = float(input("Digite a largura do terreno em metros: "))
# comprimentoLocal = float(input("Digite o comprimento do terreno em metros: "))
# presoMetroQuadrado = float(input("Digite o preço do metro quadrado: "))
# areaLocal = calcularArea(larguraLocal, comprimentoLocal)
# presoLocal = areaLocal * presoMetroQuadrado
# print(f"A área do terreno é de {areaLocal} metros quadrados")
# print(f"O preço total do terreno é de R$ {presoLocal:.2f}")



# num = [20, 30, 40, 50, 20 ,20]
# x = num.count(20)
# print(x, "vezes o número 20 aparece na lista")

# num1 = [1, 2, 6, 4, 5]
# num2 = [3, 7, 10, 8, 9]
# num1.extend(num2)
# print(num1)
# num1.sort()
# print(num1)
# num.clear()

# num = [1, 2, 3, 4, 5]
# print('tamanho da lista:', len(num))
# print('maximo:', max(num))
# print('minimo:', min(num))
# print('ordenado:', sorted(num))
# print('invertido:',reversed(num))


# class Pessoa:
#     def __init__(self, nome, idade, altura):
#         self.tudo = nome, idade, altura
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura
#     def dadosPessoa(self):
#         print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m") 

# object_pessoa_1 = Pessoa("João", 18, 1.87)
# object_pessoa_2 = Pessoa("ana", 25, 1.64)
# object_pessoa_3 = Pessoa("josé", 21, 1.78)

# print("Nome:", object_pessoa_1.tudo)
# object_pessoa_1.dadosPessoa()



class vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []
    
    def vendeu(self, vendas):
        self.vendas = vendas
        
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} não bateu a meta")
vendedor1 = input("nome do vendedor: ")
vendedor1.vendeu( input("quantidade de vendas: "))
vendedor1.bateu_meta(input("qual a meta de vendas: "))



### intervalo nada para fazer vou me incomodar com esse cadastro de novo kkkkk ###
# print("Olá! Vamos criar seu cadastro.")
# nome = input("Qual é o seu nome? ") 
# sobrenome = input("Qual é o seu sobrenome? ") 
# idade = int(input("Quantos anos você tem? "))
# email = input("Qual é o seu email? ")
# senha = input("Crie uma senha: ")
# comSenha = input("Confirme sua senha: ")
# termos = input("Você aceita os termos? (sim ou não) ")

# nomeFull = nome + " " + sobrenome
# ano_nascimento = 2025 - int(idade) # convertendo idade para inteiro

# print("Seja bem-vindo, " + nome + sobrenome + "!")
# print("Você tem ", idade, " anos.") # calculada como string

# if senha == comSenha:
#     print("Senha confirmada com sucesso.")
# else:
#     print("As senhas não coincidem. Tente novamente.")
# if termos == 'sim' or termos == 's':
#     print("Você aceitou os termos.")
# elif termos == 'não' or termos == 'nao':
#     print("Você não aceitou os termos.")
#     termos = input("Você aceita os termos? (sim ou não) ")
# else:
#     print("Resposta inválida sobre os termos.")


# print("Você nasceu em " + str(ano_nascimento) + ".") # convertendo de volta para string
# print("seus dados:", nomeFull, idade, email, senha, termos, ano_nascimento)
# print("Fim do cadastro programa.")