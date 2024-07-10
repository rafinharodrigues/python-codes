

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def beber(self, tipo_bebida):
        if tipo_bebida == 'alcolica':
            print(self.__cpf)
        print('bebendo')

    def set_cpf(self, cpf):
        self.__cpf = cpf

class Calculadora():

    def __init__(self, op: str):
        self.op = op

    def calcular(self, num1, num2):
        if self.op == '+':
            return self.__adicionar(num1, num2)
        elif self.op == '-':
            return self.__subtrair(num1, num2)

    def __adicionar(self, num1,num2):
        return num1 + num2
    
    def __subtrair(self, num1, num2):
        return num1 - num2
    
soma = Calculadora('+')
print(soma.calcular(1,1))

subtracao = Calculadora('-')
print(subtracao.calcular(1,1))
        