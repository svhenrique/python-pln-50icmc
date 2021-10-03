"""
Troque o valor da variável a por ‘1’ e verifique se o tipo da variável mudou.
"""

a = 1
b = 5.9
c = 'teste'

t1 = type(a)
for var in [a, b, c]:
    print(f'O tipo da variável com valor {var} é: {type(var)}')

a = '1'
t2 = type(a)

if t1 is not t2:
    print('Valor de a foi modificado')

