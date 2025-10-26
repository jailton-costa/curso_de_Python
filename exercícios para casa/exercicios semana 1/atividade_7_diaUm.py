#-------- contexto: Exercicio 7 de Python ---------

# Programa para calcular a densidade demográfica
# Fórmula: densidade = população / área

populacao = int(input("Digite a população total: "))
area = float(input("Digite a área em km²: "))

densidade = populacao / area  # cálculo da densidade

print(f"\nA densidade demográfica é {densidade:.2f} hab/km²")

# Verificando a classificação
if densidade > 100:
    print("Densidade Alta")
elif densidade >= 25:
    print("Densidade Média")
else:
    print("Densidade Baixa")
print("Fim do programa de densidade demográfica.")