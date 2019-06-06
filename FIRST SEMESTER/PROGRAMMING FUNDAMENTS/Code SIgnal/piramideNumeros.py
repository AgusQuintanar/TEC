import itertools
data = ('a','a','b')
grupos = []
llaves = []
for l, g in itertools.groupby(data):
    grupos.append(list(g))
    llaves.append(l)
string_modificada = []
for x in range(len(llaves)):
    string_modificada.append('('+str(len(grupos[x]))+', ' + str(llaves[x])+')')
print(' '.join(string_modificada))
