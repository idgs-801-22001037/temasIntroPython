class OperasBas:
    
    """
    public
    private
    protected
    """
    num1=0
    num2=0
    num3=0

    # constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #metodos de clases
    def suma(self):
        self.res = self.num1 + self.num2
        print(f'la suma es: {self.res}')
    
    def resta(self):
        self.res = self.num1 - self.num2
        print(f'la resta es: {self.res}')
        
    def multiplicar(self):
        self.res = self.num1 * self.num2
        print(f'la multiplicacion es: {self.res}')

    def division(self):
        self.res = self.num1 / self.num2
        print(f'la division es: {self.res}')

def main():
    obj = OperasBas(3,4)
    obj.suma()
    
if __name__ == '__main__':
    main()
    