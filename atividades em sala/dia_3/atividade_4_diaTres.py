#-------- contexto: Atividade 1 de Python - Dia 3 ---------

#04 Peça para usuário quantos números ele quer digitar, deixei ele digitar a quantidade de números guardando dentro de uma lista(use o for).
# Chame a função analisedalista. Essa função analise da lista deve apresentar a lista criada pelo usuário, original, ordem crescente, decrescente,
# excluir o primeiro número e último número e deve ao final mostrar a lista final depois de todas as mudança e o seu tamanho.

numeros = input("Quantos números você quer digitar? ")
lista_numeros = []

for i in range(int(numeros)):
    numero = float(input(f"Digite o número {i + 1}: "))
    lista_numeros.append(numero)

def analisedalista(lista):
    print('tamanho da lista:', len(lista))
    print('numero maximo:', max(lista))
    print('numero minimo:', min(lista))
    
    print("Lista original:", lista)
    print("Lista em ordem crescente:", sorted(lista))
    print("Lista em ordem decrescente:", sorted(lista, reverse=True))
    
    if len(lista) > 0:
        lista.pop(0)  # Remove o primeiro número
    if len(lista) > 0:
        lista.pop(-1)  # Remove o último número
    
    print("Lista final após remoções:", lista)
    print("Tamanho da lista final:", len(lista))
analisedalista(lista_numeros)
