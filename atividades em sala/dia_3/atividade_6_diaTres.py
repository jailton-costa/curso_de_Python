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

# ##002#
# Você vai implementar um sistema para calcular o pagamento mensal de funcionários de uma empresa que podem ter diferentes tipos de contrato:
# CLT (com salário fixo), Freelancer (com pagamento por hora) e Comissionado (salário fixo + comissão sobre vendas).
# Todos os funcionários têm nome e CPF. Funcionários CLT possuem salário fixo. Freelancers possuem valor por hora e horas trabalhadas no mês.
# Comissionados possuem salário fixo e valor total de vendas no mês.

# Atenção:
# 	- Crie uma classe base Funcionario com atributos comuns.
# 	- Crie as classes filhas FuncionarioCLT, Freelancer e Comissionado, com seus atributos específicos.
# 	- Cada classe deve implementar um método calcular_pagamento() que retorna o valor a ser pago.
# 	- Crie objetos de cada tipo, chame o método calcular_pagamento() e exiba o resultado.