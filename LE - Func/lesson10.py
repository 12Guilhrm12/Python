def media(_lista):
    var_sum = 0; 
    for i in _lista:
        var_sum+=i;

    return var_sum / len(_lista);

print(media([10, 10])); 
