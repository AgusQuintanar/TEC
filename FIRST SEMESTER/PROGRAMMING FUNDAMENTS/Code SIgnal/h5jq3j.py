s = "0.254.255.0"
b = c = 0
a = s.split('.')
for x in a:
    if not a[b].isdigit():
        c += 1
    elif int(a[b]) < 0 or int(a[b]) > 255:
        c += 1
    b += 1
if c == 0 and b == 4:
    print('true')
else:
    print('false')


