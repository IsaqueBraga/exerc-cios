def maiusculas(frase):
    string = ''
    for caracter in frase:
        if ord(caracter) >=65 and ord(caracter) <= 90:
            string += caracter
    return string
    