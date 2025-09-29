#-------- contexto: Exercício 17 de Python ---------

# 17) Cálculo de desconto por faixa de preço

valor = float(input("Digite o valor da compra: R$ "))

if 100 <= valor <= 200:
    valor_final = valor * 0.9
elif 201 <= valor <= 300:
    valor_final = valor * 0.85
elif valor > 300:
    valor_final = valor * 0.8
else:
    valor_final = valor

print(f"Valor final da compra: R$ {valor_final:.2f}")
print("Fim do programa de cálculo de desconto.")