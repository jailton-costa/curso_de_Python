#-------- contexto: Atividade 2 de Python - Dia 3 ---------

# #02Crie uma função chamada classificar_idade(idade) que receba a idade de uma pessoa e retorne uma string com a classificação:
# "Criança" (idade < 12)
# "Adolescente" (12 <= idade < 18)
# "Adulto" (18 <= idade < 60)
# "Idoso" (idade >= 60)
# No programa principal, peça a idade ao usuário, chame a função e mostre o resultado.

def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif 12 <= idade < 18:
        return "Adolescente"
    elif 18 <= idade < 60:
        return "Adulto"
    else:
        return "Idoso"

idade_usuario = int(input("Digite sua idade: "))
classificacao = classificar_idade(idade_usuario)
print("Você é classificado como:", classificacao)