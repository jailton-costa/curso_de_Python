#------ contexto: Exercícios 12 de Python ------

# Programa de operações bancárias simples

saldo = 1000.0  # saldo inicial
conta = input("Digite o número da conta: ")

print("\nEscolha a operação:")
print("1) Saldo")
print("2) Depósito")
print("3) Saque")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print(f"Saldo atual: R$ {saldo:.2f}")
elif opcao == 2:
    valor = float(input("Digite o valor do depósito: R$ "))
    saldo += valor
    print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
elif opcao == 3:
    valor = float(input("Digite o valor do saque: R$ "))
    if valor <= saldo:
        saldo -= valor
        print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente!")
else:
    print("Opção inválida!")
print("Fim do programa bancário.")