#------ contexto: Exercício 2 de Python ---------

#2) Faça um programa para ler o salário anual de um funcionário e o piso
# salarial mensal da sua categoria. Mostrar o salário mensal do funcionário
# e dizer se ele recebe de acordo com o piso (salário mensal igual ou maior
# que o piso da categoria) ou se recebe abaixo do piso.no fim mostre a paciente:
# tal possui: tal anos de idade com imc: tal

print("oii tudo bem, responda as informações abaixo:")

salario_anual = float(input("Qual é o seu salário anual ?"))
piso_salarial = float(input("Qual é o piso salarial da sua categoria ?"))
salario_mensal = salario_anual / 12

print(f"Seu salário mensal é: R$ {salario_mensal:.2f}")
if salario_mensal >= piso_salarial:
    print("Você recebe de acordo com o piso salarial da sua categoria.")
else:
    print("Você recebe abaixo do piso salarial da sua categoria.")
print("fim do programa, fique bem!")
