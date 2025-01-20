import os


def funcion1():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))

    res = num1 + num2

    print(f'Resultado: {res}')

def funcion2():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))

    res = num1 - num2

    print(f'Resultado: {res}')

opciones = """
    1 -> suma
    2 -> resta
    3 -> salir
"""

def pedirOpcion():
    opcion = int(input("Ingresa la opcion deseada: "))
    return opcion

def run():
    os.system('cls')
    seguir = True
    while seguir:
        print(opciones)
        opcion = pedirOpcion()
        if opcion == 1:
            funcion1()
        elif opcion == 2:
            funcion2()
        elif opcion == 3:
            print('ADIOS')
            seguir = False
        else:
            print("Opcion invalida")
    



if __name__ == '__main__':
    run()