# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

def zipper2(list1, list2):

    max_interval = min(len(list1),len(list2))
    return [(list1[i], list2[i]) for i in range(max_interval)]

def zipper1(list1, list2):

    if len(list1) <= len(list2):
        lower_list = list1
        second_list = list2
    else:
        lower_list = list2
        second_list = list1

    new_list = []
    for index, item in enumerate(lower_list):
        new_list.append((item, second_list[index]))

    return new_list



list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']

new_list1 = zipper1(list1,list2)
new_list2 = zipper2(list1, list2)
print(new_list1)
print()
print(new_list2)
print()
print(list(zip(list1, list2)))
print()
print(list(zip_longest(list1,list2)))