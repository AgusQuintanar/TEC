s = "Hola que hace"
s = list(s)
for caracter in range(len(s)):
    if s[caracter].islower() == True:
        s[caracter] = s[caracter].upper()
    else:
        s[caracter] = s[caracter].lower()
print(''.join(s))