a= [1, 2, 3,6, 4,5]
b= [1, 4, 3,6, 2,5]
c = []
for x in range(len(a)):
    print(a)
    print(b)
    if a[x] != b[x]:
        c.append(a[x])
        c.append(b[x])
print(c)
if a == b or c[::-1] == c:
    print('True')
else:
    print('False')