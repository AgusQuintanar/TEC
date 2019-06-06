l = [[1,2,7,0],
     [0,2,3,4],
     [0,0,4,5],
     [0,0,0,1]]


c = 0

for x in range(len(l)):
    for y in range(l[x].count(0),len(l[x])):
        if l[x][y] <= 0:
            print('falso')
        

if c == 0:
    print('true')
else:
    print('false')