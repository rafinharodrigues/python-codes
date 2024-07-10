class ControleRemoto():

    def __init__(self, televisao: str, comodo: str):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print(f'{self.televisao} avançou um canal')
    
    def voltar_canal(self):
        print(f'{self.televisao} voltou um canal')

    
    def escolher_canal(self, canal: int):
        print(f'{self.televisao} mudou para o canal {canal}')

    
controle_quarto = ControleRemoto('TV_LG', 'Quarto')
print(controle_quarto.televisao, controle_quarto.comodo)
controle_quarto.avancar_canal()
controle_quarto.voltar_canal()
controle_quarto.escolher_canal(10)