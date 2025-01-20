"""
    autor: Joel Briones
    fecha: 13/01/2024
"""


texto1 = 'HOLA'
texto2 = 'MUNDO'

textoFinal = texto1.join(texto2)

print(textoFinal)

print(f'el saludo es : {textoFinal}')

pruebaTexto = 'desarrollo web profesional'

low = pruebaTexto.lower()
up = pruebaTexto.upper()
titulo = pruebaTexto.title()
find = pruebaTexto.find('desarrollo')
contar = pruebaTexto.count('a')

split = pruebaTexto.replace('a', 'i')

separado = pruebaTexto.split(' ')

lista = [low, up, titulo, find, contar, split, separado]

def imprimirLista(lista):
    for i in lista:
        print(f'{i}')

imprimirLista(lista=lista)





