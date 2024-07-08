# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

class Person():

    def __init__(self, name, second_name='', walking=False):
        self.name = name
        self.second_name = second_name
        self.walking = walking

    def walk(self):
        if self.walking:
            print(f'{self.name} is already walking.')
            return

        print(f'{self.name} starts walking...')
        self.walking = True
        return
    
    def stop_walk(self):
        if not self.walking:
            print(f'{self.name} is not walking.')
            return
        
        print(f'{self.name} stopped walking.')
        self.walking = False
        return
    
    def complete_name(self):
        print(f'{self.name} {self.second_name}')
        return
    
p1 = Person('Andy','James')
