#------ contexto: Exercícios 1 de Python ------

# 1) Crie um programa que peça para o usuário digitar três notas
# individualmente (uma por vez), faça a média e caso a média seja igual ou
# maior que 7, mostre uma mensagem &quot;Aprovado!&quot; e a média. Caso seja
# menor que 7, mostre uma mensagem &quot;Reprovado!&quot; e a média.

print("Olá, responda as informações abaixo:")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nSua média foi: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")