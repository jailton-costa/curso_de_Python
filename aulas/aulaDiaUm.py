# Programa simples em Python que interage com o usuário

# print("olá, mundo! primeiro programa em Python")

# nome = input("Qual é o seu nome? ") 

# print("Seja bem-vindo, " + nome + "!")

# idade = int(input("Quantos anos você tem? "))

# print("Você tem ", idade, " anos.") # calculada como string

# ano_nascimento = 2025 - int(idade) # convertendo idade para inteiro

# print("Você nasceu em " + str(ano_nascimento) + ".") # convertendo de volta para string

# print("Fim do programa.")




# intervalo nada para fazer vou me incomodarr com esse cadastro
print("Olá! Vamos criar seu cadastro.")

nome = input("Qual é o seu nome? ") 
sobrenome = input("Qual é o seu sobrenome? ") 
idade = int(input("Quantos anos você tem? "))
email = input("Qual é o seu email? ")
senha = input("Crie uma senha: ")
comSenha = input("Confirme sua senha: ")
termos = input("Você aceita os termos? (sim ou não) ")

nomeFull = nome + " " + sobrenome
ano_nascimento = 2025 - int(idade) # convertendo idade para inteiro

print("Seja bem-vindo, " + nome + sobrenome + "!")
print("Você tem ", idade, " anos.") # calculada como string

if senha == comSenha:
    print("Senha confirmada com sucesso.")
else:
    print("As senhas não coincidem. Tente novamente.")

if termos == 'sim' or termos == 's':
    print("Você aceitou os termos.")
elif termos == 'não' or termos == 'nao':
    print("Você não aceitou os termos.") and termos = input("Você aceita os termos? (sim ou não) ")

else:
    print("Resposta inválida sobre os termos.")



print("Você nasceu em " + str(ano_nascimento) + ".") # convertendo de volta para string
print("seus dados:", nomeFull, idade, email, senha, termos, ano_nascimento)

print("Fim do programa.")