#-------- contexto: Exercício 22 de Python ---------

# 22) Aprovação de empréstimo bancário

valor_emprestimo = float(input("Digite o valor do empréstimo: R$ "))
salario = float(input("Digite seu salário mensal: R$ "))
anos = int(input("Número de anos para pagar: "))

parcelas = anos * 12
valor_parcela = valor_emprestimo / parcelas

if valor_parcela <= salario * 0.3:
    print(f"Empréstimo aprovado! Parcela mensal: R$ {valor_parcela:.2f}")
else:
    print("Empréstimo negado. Parcela mensal excede 30% do salário.")
print("Fim do programa de aprovação de empréstimo.")

# 22 exercícios do mal concluidos com sucesso !!! :I