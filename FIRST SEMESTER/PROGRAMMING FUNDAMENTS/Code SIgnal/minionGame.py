S = 'BANANA'
vocales = ['A','E','I','O','U']
Stuart = Kevin = 0
for caracter in range(len(S)):
    if S[caracter] not in vocales:
        Stuart += len(S)-caracter
    else:
        Kevin += len(S)-caracter
if Stuart == Kevin:
    print('Draw')
elif Stuart > Kevin:
    print('Stuart',Stuart)
else:
    print('Kevin',Kevin)
