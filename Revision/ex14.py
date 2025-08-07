n = int(input('Insira um número: ')); 
n1 = int(input('Insira um número: ')); 

try:
    r = n * n1; 
    print('Resultado da multiplicação é: ', r); 
except ZeroDivisionError:
    print('Insira um número!!!!!!!!!!'); 
    print('Bobão'); 