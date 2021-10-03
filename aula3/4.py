"""
Crie uma lista com números de 0 a 9 (em qualquer ordem). Com ela, faça: 
a.  Adicione o número 6 
b.  Insira o número 7 na 3ª posição da lista 
c.  Remova o elemento 3 da lista 
d.  Adicione o número 4 
e.  Verifique o número de ocorrências do número 4 na lista 
"""

lista = list(range(0, 10))
print(lista)

# a
lista.append(6)
print(lista)
# b
lista.insert(2, 7)
print(lista)
# c
lista.remove(3)
print(lista)
# d
lista.append(4)
print(lista)
# e
print(lista.count(4))



