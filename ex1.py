try:
    a = int(input('Digite o numerador: ')); 
    b = int(input('Digite o numerador: ')); 
    result = a / b; 
    print(f'Resultado: {result}'); 
except ValueError:
    print('Digite apenas números inteiros.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
finally:
    print('Operação realizada com sucesso.')