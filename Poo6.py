class Carro():
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

        pass

    def Acelerar(self, valor, velocidade):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

        def frear(self, valor):
            self.velocidade -= valor
            if self.velocidade < 0:
                self.velocidade = 0
                print(f"{self.modelo} reduziu para {self.velocidade} km/h")
        
        def detalhes(self):
            return (f"A marca é {self.marca},o modelo é {self.modelo},o ano é {self.ano},a cor é {self.cor},a velocidade é {self.velocidade} km/h")
        
        
carro1 = carro ("Toyota", "corola", 2020, "preto")
carro2 = carro ("honda", "civic", 2019, "vermelho")
