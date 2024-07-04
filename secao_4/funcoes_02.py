### Função que duplica o número recebido
# Modo um
def duplicate1(num):
    return num * 2

# Modo dois
def duplicate2(num):
    return f'{num}'*2

### Função que triplica o número recebido
# Modo um
def triplicate1(num):
    return num * 3

# Modo dois
def triplicate2(num):
    return f'{num}'*3


### Função que quadruplica o número recebido
# Modo um
def quadruplicate1(num):
    return num * 4

# Modo dois
def quadruplicate2(num):
    return f'{num}'*4


# print(duplicate1(2),duplicate2(2))
# print(triplicate1(2),triplicate2(2))
# print(quadruplicate1(2),quadruplicate2(2))

# Mesma função, mas com menos linhas
def calculate(num):
    def mode(mode):
        if mode == 'duplicate':
            return num * 2
        elif mode == 'triplicate':
            return num * 3
        elif mode == 'quadruplicate':
            return num * 4
        return 'Modo inválido.'

    return mode

# numero = calculate(2)
# print(numero('quadruplicate'))


# Função mais otimizada

def multiplier(multiplicador):
    
    def calculate(num):
        return multiplicador * num
    
    return calculate


duplicate = multiplier(2)
triplicate = multiplier(3)
quadruplicate = multiplier(4)

print(duplicate(3))
print(triplicate(3))
print(quadruplicate(3))



