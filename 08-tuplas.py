"""
la tupla son inmutables
se declaran con: ( )
"""

tupla = ('uno', 'dos', 'tres')
print(tupla)

print(tupla[0])

tuplas2 = (12,True, 23.5, 'el gato', 12+4j)
print(tuplas2)

tupla3 = (1,2,3,4,5,(1,2,3))
print(tupla3)

print(tupla3[1])
print(tupla3[:3])
print(tupla3[-1])

a,b,c = tupla
print(a,b,c)