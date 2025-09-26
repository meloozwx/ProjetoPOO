class Moto():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def Acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self, valor):
            self.velocidade -= valor
            if self.velocidade < 0:
                self.velocidade = 0
                print(f"{self.modelo} reduziu para {self.velocidade} km/h")

moto1 = Moto("Toyota", "corola", 2020, "preto")
moto2 = Moto("honda", "civic", 2019, "vermelho")

moto1.Acelerar(10)
moto1.frear(5)

moto2.Acelerar(13)
moto2.frear(7)
def ganhador():
     if (moto1.velocidade > moto2.velocidade):
          print(f"A moto1 ganhou")
     else:
          print(f"A moto2 ganhou")
ganhador()