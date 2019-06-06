a = '''AMBIENTE		NaturalScentsMexico	aislantes y empaques	etytec			netonline
BIOSCENTS		NaturalTrends		alejo			eurtiz			neuroservice
COMEX			PatricePatria		alethia			foxter			planelec
Clasificar		PatriceProvidencia	atmosfera		hidroagua		starkell
Fetesa			Productivity		bioener			local			tecnocor
Frescamesa		Pylsa			blen			lombra			temp
GPremier		SIIL_SYE		calidad_vida		lubritem		tracto
IVEE			SaaS_demos		cepasa			macopisa		val b loon
Loyga			SanDerma		comerdeg		marel			victor marlon
MREPS			Serur			comoplast		matec			vistaBella
Marduk			Suajespress		comunicel		maxxelec
Mexiled			TireDirect		cra			mhp
Natural			Trank			dlb			modul
NaturalScentsCoperativa	VisionCare		ethnos			naturalstore'''


a = a.split('\t')
h = []
for x in range(len(a)):
    b = a[x].strip('\n')
    c = b.split('\n')
    for y in range(len(c)):
        if c[y] != '':
            h.append(c[y])
clientes = h

rutas_clientes = []
for x in range(len(h)):
    z = h[x].replace(' ','\ ')
    rutas_clientes.append(z)

nombres_branches = []
for x in range(len(h)):
    z = h[x].replace(' ','_')
    nombres_branches.append(z)


import os
from git import Repo

ruta_del_repositorio = '/Volumes/AGUS MAC HD/SILL_WEB_PRUEBAS'
repo = Repo(ruta_del_repositorio)
assert not repo.bare

git = repo.git

ruta_carpeta_personalizaciones_del_repositorio = '/Volumes/AGUS\ MAC\ HD/SILL_WEB_PRUEBAS/Personalizaciones'
ruta_carpeta_personalizaciones_repuesto = '/Users/agusquintanar/Desktop/Personalizaciones'
ruta_del_servidor_cliente = '/Volumes/desarr/Desarrollo/Productos/Siil\ Web/Clientes/'
'''
for cliente in range(len(clientes)):
    print(50 * f'\n{clientes[cliente]}') # Imprime 50 veces el nombre del cliente en consola
    git.checkout('master') # Se cambia a la branch 'master'
    git.checkout('HEAD', b= nombres_branches[cliente]) #Se crea una nueva branch con el nombre del cliente
    git.checkout(nombres_branches[cliente]) #Se cambia a la branch del cliente generado anteriormente
    os.system(f'rm -rfv {ruta_carpeta_personalizaciones_del_repositorio}') #Se elimina la carpeta de personalizaciones del Repositorio.
    os.system(f'cp -Rv {ruta_carpeta_personalizaciones_repuesto} {ruta_del_repositorio} ')
    archivos = f'cp -Rv {ruta_del_servidor_cliente}{rutas_clientes[cliente]} {ruta_carpeta_personalizaciones_del_repositorio}'
    os.system(archivos)
    read_me_branch = open(f'Branch_{nombres_branches[cliente]}.txt','w')
    read_me_branch.write('Dentro de esta carpeta se encuentran las personalizaciones del cliente: '+clientes[cliente])
    read_me_branch.close()
    os.system('cp -Rv /Users/agusquintanar/Desktop/Final_Fundamenrtos/Branch_'+nombres_branches[cliente]+'.txt /Volumes/AGUS\ MAC\ HD/SILL_WEB_PRUEBAS/Personalizaciones')
    repo.git.add(A=True)
    git.commit('-m', 'Creacion de branch para cliente: '+clientes[cliente])

'''
for cliente in range(len(clientes)):
    print(clientes[cliente])
    git.push('origin',nombres_branches[cliente])

