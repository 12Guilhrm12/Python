def conta_vogais(_text):
    _text = _text.lower(); 
    v = "aeiouAEIOU"; 
    total = 0;
    for i in _text:
        if i in v:
            total+=1;
    return total;

print(conta_vogais("Hello World!")); 