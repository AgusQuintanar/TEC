import os
from git import Repo
import unicodedata
import subprocess

os.system('pip install --upgrade pip')
os.system('pip install git-lfs')

def convertir_string_a_lista(ls_clientes):
    a = ls_clientes
    a = a.split('\t')
    clientes = []
    for x in range(len(a)):
        b = a[x].strip('\n')
        c = b.split('\n')
        for y in range(len(c)):
            if c[y] != '' and c[y].count('.') == 0: #Elimina los archivos que no sean carpetas (Directorios)
                clientes.append(c[y])
    return clientes

def nombrar_correctamente_rutas(clientes):
    rutas_clientes = [] #Si hay espacios en los nombres de clientes, se remplazan por '\ '
    for x in range(len(clientes)):
        z = clientes[x].replace(' ','\ ')
        rutas_clientes.append(z)
    return rutas_clientes

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def nombrar_correctamente_branches(clientes):
    nombres_branches = []  #Si hay espacios en los nombres de clientes, se remplazan por '_'
    for x in range(len(clientes)):
        z = clientes[x].replace(' ','_')
        caracteres_prohibidos = "@#$&()*+"
        for char in caracteres_prohibidos:
            z = z.replace(char, "")
        z = elimina_tildes(z)
        nombres_branches.append(z)
    return nombres_branches

def verificar_nombre_producto(producto):
    while producto != 'Siil' and producto != 'Siil Web':
        print('Ingrese un nombre válido...')
        producto = input('Ingrese el nombre del producto (Siil/Siil Web): ')
    producto = producto.replace(' ', '\ ')
    return producto

def confirmar_ruta_repositorio(ruta):
    ruta_del_repositorio = ruta
    ruta_del_repositorio_confirmacion = input('Por favor confirme la ruta del repositorio: ')
    while ruta_del_repositorio != ruta_del_repositorio_confirmacion:
        print('Las rutas ingresadas no coinciden...')
        ruta_del_repositorio = input('Ingrese la ruta del repositorio: ')
        ruta_del_repositorio_confirmacion = input('Por favor confirme la ruta del repositorio: ')
    return ruta_del_repositorio

def verificar_ls(ruta_producto):
    try:
        byteOutput = subprocess.check_output(['ls', ruta_producto], timeout=2)
        return byteOutput.decode('UTF-8').rstrip()
    except subprocess.CalledProcessError as e:
        print("Error in ls -a:\n", e.output)
        return None

rojo = '\033[91m'
salmon = '\033[31m'
endcolor = '\033[0m'
verde  = '\33[32m'
amarillo = '\33[33m'
azul_bajito   = '\33[96m'
azul_agua = '\033[36m'

def creacion_branches():
    producto = verificar_nombre_producto(input('Ingrese el nombre del producto (Siil/Siil Web): '))
    producto_sin_slashes_invertidas = producto.replace('\ ',' ')
    ruta_repositorio = confirmar_ruta_repositorio(input('Ingrese la ruta del repositorio: '))
    ruta_repositorio_sin_slash_invertido = ruta_repositorio.replace('\ ',' ')
    repo = Repo(ruta_repositorio_sin_slash_invertido)
    assert not repo.bare
    git = repo.git

    ruta_del_servidor_producto_clientes = f'/Volumes/AGUS\ MAC\ HD/Clientes/'
    ruta_del_servidor_producto_clientes_sin_slash_inv = f'/Volumes/AGUS MAC HD/Clientes/'
    ls_clientes = verificar_ls(ruta_del_servidor_producto_clientes_sin_slash_inv)
    clientes = convertir_string_a_lista(ls_clientes)
    rutas_clientes = nombrar_correctamente_rutas(clientes)
    nombres_branches = nombrar_correctamente_branches(clientes)

    print(clientes)
    print(rutas_clientes)
    print(nombres_branches)
    print(nombres_branches.index('Pylsa_PurosFierros'))



    for cliente in range(141,143):
        print(f'{rojo}{clientes[cliente]}{endcolor}')  # Imprime 50 veces el nombre del cliente en consola
        git.checkout('master')  # Se cambia a la branch 'master'
        git.checkout('HEAD', b=nombres_branches[cliente])  # Se crea una nueva branch con el nombre del cliente
        git.checkout(nombres_branches[cliente])  # Se cambia a la branch del cliente generado anteriormente
        archivos = f'cp -Rv "{ruta_del_servidor_producto_clientes_sin_slash_inv}{rutas_clientes[cliente]}" {ruta_repositorio}/Personalizaciones'
        os.system(archivos)
        os.system(f'touch {ruta_repositorio}/Personalizaciones/{nombres_branches[cliente]}.txt')
        os.system(f'echo Creacion exitosa de la branch del cliente {clientes[cliente]} > {ruta_repositorio}/Personalizaciones/{nombres_branches[cliente]}.txt')
        os.system(f'git -C {ruta_repositorio} lfs install')
        os.system(f'git -C {ruta_repositorio} lfs track *')
        os.system(f'git -C {ruta_repositorio} lfs track "Personalizaciones/*.txt"')
        os.system(f'git -C {ruta_repositorio} lfs track "Personalizaciones/*.sql"')
        os.system(f'git -C {ruta_repositorio} lfs track "{ruta_repositorio}/Personalizaciones/*.txt"')
        os.system(f'git -C {ruta_repositorio} lfs track "{ruta_repositorio}/Personalizaciones/*.sql"')
        os.system(f'git -C {ruta_repositorio} lfs untrack README.md')
        repo.git.add(A=True)
        git.commit('-m', f'Creacion de branch para cliente: ' + clientes[cliente])
        print(' '+verde)
        print(f'Push en progreso de: {clientes[cliente]}')
        os.system(f'git -C {ruta_repositorio} push -u origin {nombres_branches[cliente]}')
        print(' '+endcolor)

    # git push origin --all

# /Volumes/AGUS\ MAC\ HD/SILL_WEB_PRUEBAS
# /Volumes/AGUS\ MAC\ HD/Siil
creacion_branches()