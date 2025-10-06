#-------- contexto: Atividade 6 de Python - Dia 3 ---------

# #06 ##001##
# Você deve criar um sistema para gerenciar itens de uma biblioteca. A biblioteca tem vários tipos de itens: livros, revistas e DVDs.
# Todos os itens possuem título e ano de publicação. Livros têm autor e número de páginas.
# Revistas têm número da edição e mês de publicação. DVDs têm duração em minutos e formato (ex: Blu-ray, DVD).
# Atenção:
# 	-Crie uma classe base chamada ItemBiblioteca com atributos comuns (título e ano).
# 	-Crie classes filhas: Livro, Revista e DVD, que herdam de ItemBiblioteca e possuem seus atributos específicos.
# 	-Implemente um método exibir_info() em cada classe para mostrar os detalhes do item.
# 	-Crie uma lista contendo objetos de cada tipo e imprima as informações usando o método exibir_info().

class ItemBiblioteca:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def exibir_info(self):
        return f'Título: {self.titulo}, Ano: {self.ano}'
    
class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano, autor, num_paginas):
        super().__init__(titulo, ano)
        self.autor = autor
        self.num_paginas = num_paginas

    def exibir_info(self):
        info_base = super().exibir_info()
        return f'{info_base}, Autor: {self.autor}, Número de Páginas: {self.num_paginas}'
    
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano, num_edicao, mes_publicacao):
        super().__init__(titulo, ano)
        self.num_edicao = num_edicao
        self.mes_publicacao = mes_publicacao

    def exibir_info(self):
        info_base = super().exibir_info()
        return f'{info_base}, Número da Edição: {self.num_edicao}, Mês de Publicação: {self.mes_publicacao}'
    
class DVD(ItemBiblioteca):
    def __init__(self, titulo, ano, duracao_minutos, formato):
        super().__init__(titulo, ano)
        self.duracao_minutos = duracao_minutos
        self.formato = formato

    def exibir_info(self):
        info_base = super().exibir_info()
        return f'{info_base}, Duração: {self.duracao_minutos} minutos, Formato: {self.formato}'
    
biblioteca = []
biblioteca.append(Livro("Dom Casmurro", 1899, "Machado de Assis", 256))
biblioteca.append(DVD("Avatar", 2009, 162, "Blu-ray\n"))
biblioteca.append(Revista("Scientific American", 2020, 3, "Março\n"))

for item in biblioteca:
    print(item.exibir_info())