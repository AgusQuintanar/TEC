a =  [2, 1, 10, 1]
x = 0
for e in range(len(a)-1):
    while a[e] > a[e+1]:
        print(a[e+1])
        a[e+1] += 1
        x += 1
print(x)
