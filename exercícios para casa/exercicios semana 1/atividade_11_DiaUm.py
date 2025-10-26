#------ contexto: Exercício 11 de Python ---------

# Programa que informa quantos dias tem determinado mês (sem considerar ano bissexto)

mes = int(input("Digite o número do mês (1 a 12): "))

# Usando dicionário para mapear os dias
dias_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if mes in dias_mes:
    print(f"O mês possui {dias_mes[mes]} dias.")
else:
    print("Mês inválido!")
print("Fim do programa, fique bem!")