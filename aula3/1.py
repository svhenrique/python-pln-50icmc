"""
Crie  três  variáveis  e  atribua  os  valores  a  seguir:  a=1,  b=5.9  e  c=‘teste’.  A 
partir disso, retorne o tipo de cada uma das variáveis. 
"""

a = 1
b = 5.9
c = 'teste'

for var in [a, b, c]:
    print(f'O tipo da variável com valor {var} é: {type(var)}')
