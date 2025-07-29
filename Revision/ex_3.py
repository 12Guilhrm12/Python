number   = float(input('Insira um número: ')); 
number_2 = float(input('Insira um número: ')); 

sub = number - number_2; 
div = number_2 / number; 
print(str(number) + ' - ' + str(number_2) + ' = ', sub);
print(str(number_2) + ' / ' + str(number) + ' = ', div); 

if (div < 1):
    print('False')
