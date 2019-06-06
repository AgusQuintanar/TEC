a = [1,2,3,4,5]

for x in range(6):
    a.append(a[0])
    a.pop(0)
for y in range(len(a)):
    print(a[y], end=' ')

