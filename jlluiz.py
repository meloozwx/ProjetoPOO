class Animal:
    def _init_(self,nome):
        self.nome = nome
    def falar(self):
        print("som do animal")
class Cachorro(Animal):
    def falar(self):
        print("pprt")
class Gato(Animal):
    def falar(self):
        print("miau")

Cach1 = Cachorro("Thors")
Cach1.falar()

gato1 = Gato("Nino")
gato1.falar()

