class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo="Gol", cor= "vermelho", ano= 2005)

print(vars(carro1))