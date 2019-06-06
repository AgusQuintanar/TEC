a = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbb'
for x in a:
    if a[x+1] == a[x]:
        a[x+1] = a[::-1]

print(a)