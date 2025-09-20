#-------- contexto: Atividade 4 de Python - Dia 1 ---------

# Sistema de Login Simples
# Descrição: Crie um programa que tenha um nome de usuário e uma senha predefinidos
# (ex: usuario = "admin" e senha = "12345"). O programa deve solicitar ao usuário que digite seu nome e senha.
# Se as credenciais estiverem corretas, exiba "Login bem-sucedido!". Caso contrário, mostre "Credenciais incorretas."
# Dica: Use o operador and para combinar as duas condições em um único if.

usuario_predefinido = "admin"
senha_predefinida = "12345"

print("Bem-vindo ao sistema de login!")
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_predefinido and senha == senha_predefinida:
    print("Login bem-sucedido!")

elif usuario != usuario_predefinido and senha == senha_predefinida:
    print("Nome de usuário incorreto.")

elif usuario == usuario_predefinido and senha != senha_predefinida:
    print("Senha incorreta.")

else: print("Credenciais incorretas, nome e senha errados.")