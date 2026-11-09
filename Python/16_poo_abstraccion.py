from abc import ABC , abstractmethod

class Personaje(ABC):
    @abstractmethod
    def atacar(self):
        pass

class Goku(Personaje):
    def atacar(self):
        return "Kamehameha"

goku = Goku()
print(goku.atacar)