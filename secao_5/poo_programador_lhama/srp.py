# SRP - Single Responsability Principle (S OLID)

class SistemaCadastral():

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__adiciona_no_banco(nome, idade)
        else:
            self.__mensagem_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
    
    def __adiciona_no_banco(self, nome: str, idade: int) -> None:
        print(f'"{nome}" com "{idade}" anos foi adicionado no banco')

    def __mensagem_erro(self) -> None:
        print('Informações inválidas!')
    
sc = SistemaCadastral()
sc.cadastrar('Marcelo', 20)
    