s = 'cde'
s2 = 'abc'

a = list(s)
b = list(s2)
c = 0
for x in range(len(a)):
    if a[x] in b:
        c += 1

print(len(a)+len(b)-2*c)