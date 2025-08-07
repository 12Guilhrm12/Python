lista = [1, 2, 3, 4, 5]; 
try:
    n = int(input('Escolha um número entre 1 e 5: ')); 
    print(lista[n]); 
except IndexError:
    print('Insira um valor dentro do intervalo!'); 
