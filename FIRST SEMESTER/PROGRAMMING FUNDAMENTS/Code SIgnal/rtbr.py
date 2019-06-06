picture = ["abcde","fghij","klmno","pqrst","uvwxy"]

picture.insert(0,((len(picture[0]))*'*'))
picture.append(((len(picture[0]))*'*'))
for x in range(len(picture)):
    picture[x] = '*'+picture[x]+'*'


print(picture)

