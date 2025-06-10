try:
    a = float(input('Digite o multiplicando: ')); 
    b = float(input('Digite o multiplicador: ')); 
    result = a * b; 
    print(f'Resultado: {result}'); 
except ValueError:
    print('Digite apenas números inteiros.')
finally:
    print('Operação realizada com sucesso.')