"""
Crie um arquivo e: 
a.  Escreva nele os números de 1 a 10 
b.  Depois de escrito, imprima na tela todos os números do arquivo 
c.  Escreva no arquivo os números de 11 a 20, substituindo os números que 
estavam antes no arquivo 
d.  Escreva no arquivo os números de 21 a 30, adicionando os números no 
final do arquivo (sem apagar o que já estavam lá) 
e.  Imprima na tela todos os números do arquivo novamente (de 11 a 30) 
f. Imprima  na  tela  todos  os  números  do  arquivo  novamente,  mas  agora 
linha por linha
"""

def get_numbers(a, b):
    numbers = ''
    for number in list(range(a, b)):
        numbers += str(number) + ' '
    numbers = numbers[:len(numbers)-1]
    return numbers

with open('myfile.txt', 'x') as f:
    numbers = get_numbers(1, 11)
    f.write(numbers + '\n')

with open('myfile.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    numbers = get_numbers(11, 21)
    f.write(numbers + '\n')
    f.read()
    numbers = get_numbers(21, 31)
    f.write(numbers + '\n')
    f.seek(0)
    print(f.read())
    f.seek(0)
    for line in f:
        print(line, end='')

