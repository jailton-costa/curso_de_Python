#-------- contexto: Exercicio 19 de Python ---------

# 19) Preço do ingresso com descontos

preco_base = 20.0
idade = int(input("Digite sua idade: "))

desconto = 0

if idade <= 12:
    desconto = 0.5  # 50% desconto
elif idade > 60:
    desconto = 0.3  # 30% desconto

estudante = input("Você é estudante? (S/N): ").upper()
if estudante == "S":
    desconto = max(desconto, 0.25)  # 25% desconto para estudante

preco_final = preco_base * (1 - desconto)
print(f"Valor do ingresso: R$ {preco_final:.2f}")
print("Fim do programa de cálculo de ingresso.")