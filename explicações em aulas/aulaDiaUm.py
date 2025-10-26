# Aula 1 de Python 📘
# Conteúdo:
# - [x] `if`, `else`, `elif`
# - [x] validação de entrada
# - [x] interação com o usuário (input e print)
# - [x] tipos de dados (string, int, float)
# - [x] conversão de tipos (str(), int(), float())


# Programa simples em Python que interage com o usuário
# print("olá, mundo! primeiro programa em Python")
# nome = input("Qual é o seu nome? ") 
# print("Seja bem-vindo, " + nome + "!")
# idade = int(input("Quantos anos você tem? "))
# print("Você tem ", idade, " anos.") # calculada como string
# ano_nascimento = 2025 - int(idade) # convertendo idade para inteiro
# print("Você nasceu em " + str(ano_nascimento) + ".") # convertendo de volta para string
# print("Fim do programa.")


## intervalo nada para fazer vou me incomodar com esse cadastro ###
print("Olá! Vamos criar seu cadastro.")
nome = input("Qual é o seu nome? ") 
sobrenome = input("Qual é o seu sobrenome? ") 
idade = int(input("Quantos anos você tem? "))
email = input("Qual é o seu email? ")
while True:
    senha = input("Digite a senha: ")
    comSenha = input("Confirme a senha: ")

    if senha == comSenha:
        print("Senha confirmada com sucesso.")
        break 
    else:
        print("As senhas não coincidem. Tente novamente.\n")

while True:
    termos = input("Você aceita os termos? (sim ou não) ").strip().lower()

    if termos == 'sim' or termos == 's':
        print("Você aceitou os termos.")
        break 
    elif termos == 'não' or termos == 'nao' or termos == 'n':
        print("Você não aceitou os termos. Por favor, aceite para continuar.\n")
    else:
        print("Resposta inválida sobre os termos. Responda com 'sim' ou 'não'.\n")


nomeFull = nome + " " + sobrenome
ano_nascimento = 2025 - int(idade) 

print("Seja bem-vindo, " + nomeFull + "!")
print("Você tem ", idade, " anos.") 

print(f"seus dados:\n nome: {nomeFull}\n, idade: {idade}\n, email: {email}\n, senha: {senha}\n, termos: {termos}\n, data de naciento: {ano_nascimento} \n Fim do cadastro programa.")
## cadastro finalizado com sucesso! :)