class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        print(f'Área: {self.base * self.altura}')
    
    def calcular_perimetro(self):
        print(f'Perímetro: {2 * (self.base + self.altura)}')
    
retangulo = Retangulo(10, 10)

retangulo.calcular_area()
retangulo.calcular_perimetro()