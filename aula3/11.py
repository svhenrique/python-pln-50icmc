"""
Crie um dicionário com 5 entradas e suas respectivas chaves e valores. Faça: 
a.  Imprima todas as chaves do dicionário 
b.  Imprima todos os valores do dicionário 
c.  Imprima todos os itens do dicionário 
d.  Imprima o 2º item do dicionário 
e.  Imprima o dicionário completo 
f. Percorra o dicionário, imprimindo para cada entrada o modelo “(chave) 
tem como valor (valor)”
"""

values = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# a
print(values.keys())

# b
print(values.values())

# c
for key in values:
    print(values[key], end=" ")
print()

# d
print(list(values.values())[1])

# e
print(values)

# f
for key in values:
    print(key, " tem como valor ", values[key])
