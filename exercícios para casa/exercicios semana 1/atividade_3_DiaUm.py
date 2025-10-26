#-------- contexto: Exercício 3 de Python ---------

# 3) Criar um programa que pergunte o nome e a idade da pessoa, e se tem
# comorbidade (S ou N). Mostrar mensagem "Pode se vacinar!" caso a
# idade seja maior ou igual a 60 ou tenha comorbidade. Caso contrário,
# mostrar mensagem "Não pode se vacinar".

print("olá, cliente tudo bem! responda as informações abaixo:")
nome = input("Qual é o seu nome ?")
nomeV = input("Qual é o nome do vendedor ?")
produto = input("Qual é o nome do produto ?")
valor = float(input("Qual é o valor do produto ?"))

desconto = valor * 0.2
comissao = valor * 0.04
valorFinal = valor - desconto
valorVendedor = comissao

print("o cliente: ",nome," comprou o produto: ",produto," e pagou com 20% de desconto o valor de: ",valorFinal)
print("o vendedor: ",nomeV," ganhou de comiçao o valor de: ",valorVendedor)
print("fim do programa, volte sempre!")