# Função que multiplica todos os argumentos não nomeados recebidos
def multiplica(*args):
    result = 1

    for numero in args:
        result *= numero
    
    return result

# print(multiplica(3,2,5,10,-1))

# Função que retorna se um número é par ou ímpar

def paridade(num):
    par = 'Este número é par.'
    impar = 'Este número é ímpar.'

    return par if num % 2 == 0 else impar

print(paridade(16))
