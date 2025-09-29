#Q3
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario



class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento


g = Gerente("Ana", 5000, "TI")
print(g.nome, g.salario, g.departamento)
