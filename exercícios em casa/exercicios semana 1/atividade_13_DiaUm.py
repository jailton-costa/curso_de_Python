#------ contexto: Exercícios 13 de Python ------

# Programa para calcular valor final da compra com base em categoria de assinante

valor_compra = float(input("Digite o valor da compra: R$ "))
print("Escolha a categoria de assinante:")
print("1 - Assinante diamante (20% desconto e frete grátis)")
print("2 - Assinante ouro (20% desconto e paga frete)")
print("3 - Assinante prata (10% desconto e paga frete)")
print("4 - Não assinante (sem benefícios)")

categoria = int(input("Digite a opção (1, 2, 3 ou 4): "))
frete = 12.50

if categoria == 1: 
    valor_final = valor_compra * 0.8  
elif categoria == 2:
    valor_final = valor_compra * 0.8 + frete
elif categoria == 3: 
    valor_final = valor_compra * 0.9 + frete
elif categoria == 4: 
    valor_final = valor_compra + frete
else:
    print("Categoria inválida!")
    valor_final = None

if valor_final is not None:
    print(f"Valor final da compra: R$ {valor_final:.2f}")
print("Fim do programa de cálculo de compra.")