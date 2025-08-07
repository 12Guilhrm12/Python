n = int(input('Insira um número: ')); 
n1 = int(input('Insira um número: ')); 

try:
    r = n / n1; 
    print('Resultado da divisão é: ', r); 
except ZeroDivisionError:
    print('Você não pode dividir por zero'); 
    print('Bobão');