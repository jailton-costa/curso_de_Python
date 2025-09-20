#-------- contexto: Atividade 6 de Python - Dia 1 ---------

# ####Cálculo de Preço de Combustível####
# Descrição: Desenvolva um programa que pergunte ao usuário o tipo de combustível (Gasolina ou Alcool) e a quantidade de litros abastecida. O programa deve calcular o valor total a ser pago, considerando os preços e descontos a seguir:
# Álcool:
# Preço por litro: R$ 4.50.
# Desconto de 3% para até 20 litros.
# Desconto de 5% para mais de 20 litros.
# Gasolina:
# Preço por litro: R$ 5.80.
# Desconto de 4% para até 20 litros.
# Desconto de 6% para mais de 20 litros.
# Dica: Use condições aninhadas (if dentro de if) para verificar o tipo de combustível e a quantidade de litros, aplicando o desconto correto.
# Exemplo de Saída:
# Combustível: Alcool, Litros: 15. Saída: "Valor a pagar: R$ 65.59" (preço original R$ 67.50, desconto de 3%)
# Combustível: Gasolina, Litros: 30. Saída: "Valor a pagar: R$ 163.68" (preço original R$ 174.00, desconto de 6%)

print("Bem-vindo ao sistema de combustivel!")

combustivel = input("Qual o tipo de combustivel (Gasolina ou Alcool)? ").strip().lower()

litros = float(input("Quantos litros foram abastecidos? "))

valor = 0

if combustivel == 'alcool':
    valor = litros * 4.50
    if litros <= 20:
        desconto = valor * 0.03
    else:
        desconto = valor * 0.05
    valor_final = valor - desconto
    print(f"Combustível: Alcool, Litros: {litros}. Valor a pagar: R$ {valor_final:.2f} (preço original R$ {valor:.2f}, desconto de R$ {desconto:.2f})")

elif combustivel == 'gasolina':
    valor = litros * 5.80
    if litros <= 20:
        desconto = valor * 0.04
    else:
        desconto = valor * 0.06
    valor_final = valor - desconto
    print(f"Combustível: Gasolina, Litros: {litros}. Valor a pagar: R$ {valor_final:.2f} (preço original R$ {valor:.2f}, desconto de R$ {desconto:.2f})")

else: print("Tipo de combustível inválido. Por favor, escolha 'Gasolina' ou 'Alcool'.")