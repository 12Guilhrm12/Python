def eh_palindromo(_text):
    if (_text.lower() == _text.lower()[::-1]):
        return True;
    else:
        return False;

print(eh_palindromo("omissíssimo")); 