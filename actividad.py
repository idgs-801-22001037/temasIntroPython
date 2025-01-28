

class Distancia:
    """x2 = 0
    x1 = 0
    y2 = 0
    y1 = 0"""
    def __init__(self):
        self.x2 = 0
        self.x1 = 0
        self.y2 = 0
        self.y1 = 0
    def pedir(self):
        self.x2 = int(input('ingrese la coordenada x2: '))
        self.x1 = int(input('ingrese la coordenada x1: '))
        self.y2 = int(input('ingrese la coordenada y2: '))
        self.y1 = int(input('ingrese la coordenada y1: '))
        
    def calcular(self):
        self.res = (( self.x2-self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print(f' el resultado es: {self.res}')
   
def main():
    
    distancia = Distancia()
    distancia.pedir()
    distancia.calcular()
if __name__ == '__main__':
    main()