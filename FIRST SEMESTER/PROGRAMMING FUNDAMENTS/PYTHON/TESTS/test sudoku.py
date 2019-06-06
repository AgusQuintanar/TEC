def sudokuCheck(path):
    file = open(path,'r')
    content = file.read()
    a = content.replace('\n','')
    b = a.replace(',','')

    return b

error = 0
path = 'sudoku1.txt'
sudoku = list(sudokuCheck(path))


horizontales = [0,1,2,3,4,5,6,7,8]
verticales = [0,9,18,27,36,45,54,63,72]
cuadrantes = [0,1,2,9,10,11,18,19,20]

lista_horizontal = []
lista_vertical = []
lista_cuadrante = []

for x in range(len(horizontales)):

    l_hor = []
    l_ver = []
    l_cua = []
    for y in range(len(horizontales)):
        l_hor.append(sudoku[horizontales[y]])
        l_ver.append(sudoku[verticales[y]])
        l_cua.append(sudoku[cuadrantes[y]])

        horizontales[y] += 9
        verticales[y] += 1
        if cuadrantes[y]+1 % 12 == 0:
            cuadrantes[y] += 18
        else:
            cuadrantes[y] += 3

    lista_horizontal.append(l_hor)
    lista_vertical.append(l_ver)
    lista_cuadrante.append(l_cua)


print(lista_horizontal)
print(lista_vertical)
print(lista_cuadrante)