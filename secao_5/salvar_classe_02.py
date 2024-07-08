# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
import salvar_classe_01

def save_data(instance): 
    
    with open('data.json', 'w', encoding='utf8') as file:
        data = vars(instance)
        json.dump(data,file,indent=2)
    
    print('Instance data saved.')
    return


def load_data(file):

    with open(file, 'r', encoding='utf8') as file:
        data = json.load(file)

    return data


p1 = salvar_classe_01.p1

save_data(p1)

file = 'data.json'
data_loaded = load_data(file)

new_instance = salvar_classe_01.Person(
                                       name=data_loaded['name'],
                                       second_name=data_loaded['second_name'],
                                       walking=data_loaded['walking']
                                       )

print(new_instance.name)
print(new_instance.second_name)
new_instance.complete_name()
print(vars(new_instance))