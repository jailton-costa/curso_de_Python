#-------- contexto: Atividade 5 de Python - Dia 3 ---------

#05 Criar uma classe que representa uma garrafa de água e permite enchê-la ou beber dela. Criar uma classe Garrafa.
# A garrafa tem: um atributo volume (inicialmente começa vazia, ou seja, 0). Métodos: encher(): coloca água na garrafa até 100.
# beber(qtd): diminui a quantidade de água se houver suficiente. mostrar_volume(): mostra quanto de água há na garrafa.
class Garrafa:
    def __init__(self):
        self.volume = 0  # Volume inicial da garrafa em ml

    def encher(self):
        self.volume = 1000  # Enche a garrafa até 1000 ml
        print("A garrafa foi enchida. Volume atual:", self.volume, "ml")

    def beber(self, qtd):
        if qtd <= self.volume:
            self.volume -= qtd
            print(f"Você bebeu {qtd} ml. Volume restante:", self.volume, "ml")
        else:
            print("Não há água suficiente na garrafa para beber essa quantidade.")

    def mostrar_volume(self):
        print("Volume atual da garrafa:", self.volume, "ml")

minha_garrafa = Garrafa()
minha_garrafa.encher()
minha_garrafa.mostrar_volume()
minha_garrafa.beber(250)
minha_garrafa.mostrar_volume()
minha_garrafa.beber(800)
minha_garrafa.mostrar_volume()
minha_garrafa.beber(100)
minha_garrafa.mostrar_volume()
minha_garrafa.encher()
minha_garrafa.mostrar_volume()