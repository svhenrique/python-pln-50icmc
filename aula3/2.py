"""
Crie  três  variáveis  e  atribua  os  valores  a  seguir:  a=1,  b=5.9  e  c=‘teste’.  A 
partir disso, retorne o tipo de cada uma das variáveis. 
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

