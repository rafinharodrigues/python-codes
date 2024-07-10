

class Alarme():

    def __init__(self) -> None:
        self.__estado = False

    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, estado: bool) -> None:
        self.__estado = estado

alarme1 = Alarme()
print(alarme1.get_estado())
alarme1.set_estado(True)
print(alarme1.get_estado())
