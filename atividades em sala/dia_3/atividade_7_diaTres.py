#-------- contexto: Atividade 7 de Python - Dia 3 ---------

#07##002#
# Você vai implementar um sistema para calcular o pagamento mensal de funcionários de uma empresa que podem ter diferentes tipos de contrato:
# CLT (com salário fixo), Freelancer (com pagamento por hora) e Comissionado (salário fixo + comissão sobre vendas).
# Todos os funcionários têm nome e CPF. Funcionários CLT possuem salário fixo. Freelancers possuem valor por hora e horas trabalhadas no mês.
# Comissionados possuem salário fixo e valor total de vendas no mês.

# Atenção:
# 	- Crie uma classe base Funcionario com atributos comuns.
# 	- Crie as classes filhas FuncionarioCLT, Freelancer e Comissionado, com seus atributos específicos.
# 	- Cada classe deve implementar um método calcular_pagamento() que retorna o valor a ser pago.
# 	- Crie objetos de cada tipo, chame o método calcular_pagamento() e exiba o resultado.

class Funcionario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_info(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'

    def calcular_pagamento(self):
        return 0

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

    def exibir_info(self):
        info = super().exibir_info()
        return f'{info}, Tipo: CLT, Pagamento: R${self.calcular_pagamento():.2f}'

class Freelancer(Funcionario):
    def __init__(self, nome, cpf, valor_hora, horas_trabalhadas):
        super().__init__(nome, cpf)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas

    def exibir_info(self):
        info = super().exibir_info()
        return f'{info}, Tipo: Freelancer, Pagamento: R${self.calcular_pagamento():.2f}'

class Comissionado(Funcionario):
    def __init__(self, nome, cpf, salario_fixo, vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self.salario_fixo = salario_fixo
        self.vendas = vendas
        self.percentual_comissao = percentual_comissao 

    def calcular_pagamento(self):
        return self.salario_fixo + (self.vendas * self.percentual_comissao)

    def exibir_info(self):
        info = super().exibir_info()
        return f'{info}, Tipo: Comissionado, Pagamento: R${self.calcular_pagamento():.2f}'


funcionarios = [
    FuncionarioCLT("Jaja", "00000", 1460),
    Freelancer("Sam", "22222", 55, 40),        
    Comissionado("Max", "11111", 3000, 10000, 0.10)  
]

for f in funcionarios:
    print(f.exibir_info())

total = sum(f.calcular_pagamento() for f in funcionarios)
print(f"\n💰 Total pago pela empresa: R${total:.2f}")
