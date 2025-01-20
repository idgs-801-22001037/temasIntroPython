"""x = 0


while x<10:
    print(x)
    
    """
    
    
num1 = int(input('Ingresa el numero 1: '))
num2 = int(input('Ingresa el numero 2: '))

variable = num2
array = []
while(variable > 0):
    array.append(str(num2))
    variable = variable - 1

for salida in array:
    print(salida + ' + ', end='')

resultado = num1 * num2

print(salida, ' = ' , resultado) 