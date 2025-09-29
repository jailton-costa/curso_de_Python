#-------- contexto: Exercicio 5 de Python ---------

# 5) Criar um programa que simule o login de um roteador. O nome de
# usuário (username) é &quot;admin&quot; e a senha (password) &quot;123&quot;. Pedir ao
# usuário para digitar username e password. Caso os dados estejam
# corretos, mostrar uma mensagem &quot;Login efetuado!&quot;, caso contrário
# &quot;Login falhou!&quot;. (DESAFIO: Mostrar mensagens específicas para erro de
# username, de password ou de ambos).

print("Bem-vindo ao sistema de login!")
usuario_predefinido = "admin"
senha_predefinida = "123"
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_predefinido and senha == senha_predefinida:
    print("Login efetuado!")

elif usuario != usuario_predefinido and senha == senha_predefinida:
    print("Nome de usuário incorreto.")

elif usuario == usuario_predefinido and senha != senha_predefinida:
    print("Senha incorreta.")

else:
    print("Login falhou!") 