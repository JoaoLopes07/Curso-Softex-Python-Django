from math import pi

class Circulo():
    def __init__(self, raio: int):
        if raio <0:
            print('O raio não pode ser negativo')
            self._raio = 0
        else:
            self._raio = raio

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, novo_raio: int):
        if novo_raio >0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print('Digite um número positivo')

    def calcular_area(self):
        if self.raio > 0:
            area = pi * self.raio**2
            print(f'Área: {area:.2f}')




rodar = Circulo(-10)
print(f'Raio: {rodar.raio}')
rodar.raio = -5
rodar.calcular_area()
