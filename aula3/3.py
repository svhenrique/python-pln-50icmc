"""
Faça a soma da variável b com a variável c. Interprete a saída, tanto em caso 
de execução correta quanto em caso de execução com erro. 
"""

a = 1
b = 5.9
c = 'teste'

if type(b) is type(c):
    result = b + c
    print(result)   
    print('Soma executada com sucesso!')
else:
    print('Tipos de variável são diferentes, logo, não é possível somar')
