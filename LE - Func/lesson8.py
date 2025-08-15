def fatorial(_number):
    fatoracao = 1
    for i in range(_number):
        fatoracao = fatoracao * (i + 1); 

    return fatoracao; 

x = int(input('Insira um número: ')); 
fat = fatorial(x); 

print(fat); 
