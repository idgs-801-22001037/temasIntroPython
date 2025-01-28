from pathlib import Path

#texto = open('archivo.txt','a')
#texto.write('Hola, mundo\n')
texto = open('archivo.txt', 'r')
lineas = texto.readlines()
#linea = texto.readline()
#print(linea)
print(lineas)
#print(type(linea))
print(type(lineas))
for letra in lineas:
    print(letra)
texto.close()

"""
menu
ingreasar o salir
pedir nombre, personas y numero boletos
verificar las condiciones que no se pasen las personas
si se pasa lanza menu que diga, no puedes comprar mas de 7 por perso
cambiar numero perso o boletos

pagar con efectivo o tarhjeta 
mostrar el total a pagar con las condiciones de la 

si digo terminar esa compra con nombre y total se almacena el archivo de txt

mostar total ventas y por cada uno


"""