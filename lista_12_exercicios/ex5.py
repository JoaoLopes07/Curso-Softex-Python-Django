class Carro():
    def __init__(self, modelo, nivel_combustivel = 0):
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel
        
    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f'Abasteceu {litros}litros')
    
    def dirigir(self, distancia):
        consumo = distancia / 10
        if self.nivel_combustivel >= consumo:
            self.nivel_combustivel -= consumo
            print(f'O carro {self.modelo} andou {distancia}km')
            
        else:
            print('Não tem combustivel suficiente')

carro = Carro('Onix')

carro.abastecer(10)
carro.dirigir(50)
carro.dirigir(60)
    