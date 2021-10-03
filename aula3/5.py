"""
Ainda com a lista criada na questão anterior, faça: 
a.  Retorne os primeiros 3 elementos da lista 
b.  Retorne os elementos que estão da 3ª posição até a 7ª posição da lista 
c.  Retorne os elementos da lista de 3 em 3 elementos 
d.  Retorne os 3 últimos elementos da lista 
e.  Retorne todos os elementos menos os 4 últimos da lista
"""

lista = list(range(0, 10))

# a
print(lista[:3])

# b
print(lista[2:7])

# c
print(lista[::3])

# d
print(lista[len(lista)-3:])

# e
print(lista[:len(lista)-4])



