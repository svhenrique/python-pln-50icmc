"""
Crie uma tupla com números de 0 a 9 (em qualquer ordem) e tente: 
a.  Alterar o valor do 3º elemento da tupla para o valor 10 
b.  Verificar o índice (posição) do valor 5 na tupla
"""
values = tuple(range(0, 10))

# b 
print(values.index(5))

# a
values[2] = 4 


