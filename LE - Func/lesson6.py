def eh_par(_number):
    if (_number % 2 == 0):
        return True;
    elif (_number % 2 != 0):
        return False;

x = int(input('Insira um número: ')); 

par = bool(eh_par(x)); 
print(par); 