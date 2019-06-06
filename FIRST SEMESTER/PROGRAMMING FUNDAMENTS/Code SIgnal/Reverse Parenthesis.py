s = "abc(cba)ab(bac)c"

z = list(s)
index1 = []
index2 = []
orden = []
q = s.count('(')
for x in range(len(s)):
    if z[x] == ')':
        index1.append(0)
        index1.append(x+1)
    if z[x] == '(':
        index1.append(x+1)
print(index1)
for y in range(len(index1)-2*q):
    if index1[y] == 0 and index1[y+1] != 0 and index1[y+2] != 0 and index1[y+3] == 0:
        w = index1[y + 1]
        index1.insert(y+5, w)
        index1.pop(y+1)

print(index1)
index1 = [elemento for elemento in index1 if elemento !=0]
print(index1)


for e in range(len(index1)//2):
    index2.append(index1[e])
for e in range(len(index1)//2):
    index1.pop(0)
index2 = index2[::-1]
for x in range(len(index1)):
    z[index2[x]:index1[x]] = z[index2[x]:index1[x]][::-1]

print(index1)
print(index2)


z = ''.join(z)
e = z.replace(')','')
r = e.replace('(','')
print(r)

# [19, 25, 46, 51]