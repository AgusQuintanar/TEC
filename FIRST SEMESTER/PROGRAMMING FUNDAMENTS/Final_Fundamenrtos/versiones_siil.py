import os
from git import Repo
a = '''
Abal				GEM				Obtej
Adm_Reciclados			Gamacolor			One World
AislantesyEmpaques		General_Tools			Orbis
Albaosa				GlobalMark			PYLSA7_Reciclados
Alejo				GlobalTelecom2			PacoMarquez
Alethia				Gpremier			Pass.xls
AltoDiseno			GrupoAllen			Patrice
Apprende			GrupoLoyga			PatriceProvidencia
Artexport			Hidroagua			Pepinos Ocampo
AsAvBasc			IETSA				Pes
Atlantida			IVEE				Pidellantas
Atmosfera			Identidad			Planelec
BOSCHA				Impulso				Premier
Bea				Innova				PromFarmacos
BigBang				Innovika			Promographic
Bioener				JFP				PylsaFerroso
Blen				Jela				PylsaMaDolores
Bodeguero			Jordao				Pylsa_PurosFierros
Bogavante			Jorge_José_María		ReActiv
Bomba				Jyx				Refill
Boxmart				Klimet				RitaGabrielaLopezCampero
COMERDEG_SODE			Kumho				RosendoPacheco
CP43				La Canasta			SDP
CVA				La Squina			Sahar
Carbotecnia			LaBellota			Saplagsa
Careintra			La_Espanola			Saramel
CasaEsthnos			Lan&Wan				Sep
CasaEstrada			LlantasDirectas			Serur
CentroSerur			Lombra				SolucionesTecnologicas
Cepasa				Los Parques			Starkell
Charmee				Lubritem			Stil Mobil
Chilerito			MReps				Suajespress
Citlali				MULLER				SuperVic
Comercializadora_y_Reciclados	Macarmenarandiaabascal		TTapatias
ComexModa			Macopisa			TYB
Comoplast			Malpica				Tecnocard
Compurama			Mape				Tecnocargo
Comunicel			Marduk				Tecnomuebles
Connext				Marel				TireDirect
Copident			MaríaDolores			Tractocamiones
Crea_Pylsa			MartinPacheco			TranK
CuspideEmp			Matec				VRM Innovations
DLBControl			MatecCanada			Val_B_Loon
'''
clientes = ['Abal', 'GEM', 'Obtej', 'Adm_Reciclados', 'Gamacolor', 'One_World', 'AislantesyEmpaques', 'General_Tools',
       'Orbis', 'Albaosa', 'GlobalMark', 'PYLSA7_Reciclados', 'Alejo', 'GlobalTelecom2', 'PacoMarquez', 'Alethia',
       'Gpremier', 'AltoDiseno', 'GrupoAllen', 'Patrice', 'Apprende', 'GrupoLoyga', 'PatriceProvidencia',
       'Artexport', 'Hidroagua', 'Pepinos_Ocampo', 'AsAvBasc', 'IETSA', 'Pes', 'Atlantida', 'IVEE', 'Pidellantas',
       'Atmosfera', 'Identidad', 'Planelec', 'BOSCHA', 'Impulso', 'Premier', 'Bea', 'Innova', 'PromFarmacos', 'BigBang',
       'Innovika', 'Promographic', 'Bioener', 'JFP', 'PylsaFerroso', 'Blen', 'Jela', 'PylsaMaDolores', 'Bodeguero',
       'Jordao', 'Pylsa_PurosFierros', 'Bogavante', 'Jorge_José_María', 'ReActiv', 'Bomba', 'Jyx', 'Refill', 'Boxmart',
       'Klimet', 'RitaGabrielaLopezCampero', 'COMERDEG_SODE', 'Kumho', 'RosendoPacheco', 'CP43', 'La_Canasta', 'SDP',
       'CVA', 'La_Squina', 'Sahar', 'Carbotecnia', 'LaBellota', 'Saplagsa', 'Careintra', 'La_Espanola', 'Saramel',
       'CasaEsthnos', 'Lan_Wan', 'Sep', 'CasaEstrada', 'LlantasDirectas', 'Serur', 'CentroSerur', 'Lombra',
       'SolucionesTecnologicas', 'Cepasa', 'Los_Parques', 'Starkell', 'Charmee', 'Lubritem', 'Stil_Mobil',
       'Chilerito', 'MReps', 'Suajespress', 'Citlali', 'MULLER', 'SuperVic', 'Comercializadora_y_Reciclados',
       'Macarmenarandiaabascal', 'TTapatias', 'ComexModa', 'Macopisa', 'TYB', 'Comoplast', 'Malpica', 'Tecnocard',
       'Compurama', 'Mape', 'Tecnocargo', 'Comunicel', 'Marduk', 'Tecnomuebles', 'Connext', 'Marel', 'TireDirect',
       'Copident', 'MaríaDolores', 'Tractocamiones', 'Crea_Pylsa', 'MartinPacheco', 'TranK', 'CuspideEmp', 'Matec',
       'VRM_Innovations', 'DLBControl', 'MatecCanada', 'Val_B_Loon', 'Damy', 'MayCard', 'Vegsa', 'Dapesa', 'Mexiled',
       'VictorMarlon', 'Deleites', 'Mhp', 'VisionCare', 'Diseco', 'Mobel', 'Vistabella', 'Dist.XP', 'Modul', 'Vitanova',
       'Divemex', 'Monier', 'as', 'ElRosario', 'Montana', 'aspinet', 'Estatec', 'MovilParts', 'cct', 'Estrasol',
       'Multillantas', 'constantinoramonTecnocor', 'Etytec', 'Nafarrate', 'foxtertools', 'Eurollantas', 'Naresa',
       'isquisa', 'Evolution', 'Natco', 'isquisa2', 'Expormex', 'Nattura', 'metrologiaaplicada', 'FarmaciaZamora',
       'NaturalBioscents', 'nutrimentosquer', 'Fastec', 'NaturalScents_Store', 'pounce', 'FerreteriaTejeda',
       'NaturalTrends', 'scr', 'Ficachi', 'Nestori', 'sistecom', 'Finezza', 'NetOnline(HéctorMagno)', 'sye', 'Franco',
       'Net_Communication', 'tecno', 'G&B', 'Neuroservice']


ruta_clientes = ['Abal', 'GEM', 'Obtej', 'Adm_Reciclados', 'Gamacolor', 'One\ World', 'AislantesyEmpaques', 'General_Tools',
       'Orbis', 'Albaosa', 'GlobalMark', 'PYLSA7_Reciclados', 'Alejo', 'GlobalTelecom2', 'PacoMarquez', 'Alethia',
       'Gpremier', 'AltoDiseno', 'GrupoAllen', 'Patrice', 'Apprende', 'GrupoLoyga', 'PatriceProvidencia',
       'Artexport', 'Hidroagua', 'Pepinos\ Ocampo', 'AsAvBasc', 'IETSA', 'Pes', 'Atlantida', 'IVEE', 'Pidellantas',
       'Atmosfera', 'Identidad', 'Planelec', 'BOSCHA', 'Impulso', 'Premier', 'Bea', 'Innova', 'PromFarmacos', 'BigBang',
       'Innovika', 'Promographic', 'Bioener', 'JFP', 'PylsaFerroso', 'Blen', 'Jela', 'PylsaMaDolores', 'Bodeguero',
       'Jordao', 'Pylsa_PurosFierros', 'Bogavante', 'Jorge_José_María', 'ReActiv', 'Bomba', 'Jyx', 'Refill', 'Boxmart',
       'Klimet', 'RitaGabrielaLopezCampero', 'COMERDEG_SODE', 'Kumho', 'RosendoPacheco', 'CP43', 'La\ Canasta', 'SDP',
       'CVA', 'La\ Squina', 'Sahar', 'Carbotecnia', 'LaBellota', 'Saplagsa', 'Careintra', 'La_Espanola', 'Saramel',
       'CasaEsthnos', 'Lan&Wan', 'Sep', 'CasaEstrada', 'LlantasDirectas', 'Serur', 'CentroSerur', 'Lombra',
       'SolucionesTecnologicas', 'Cepasa', 'Los\ Parques', 'Starkell', 'Charmee', 'Lubritem', 'Stil\ Mobil',
       'Chilerito', 'MReps', 'Suajespress', 'Citlali', 'MULLER', 'SuperVic', 'Comercializadora_y_Reciclados',
       'Macarmenarandiaabascal', 'TTapatias', 'ComexModa', 'Macopisa', 'TYB', 'Comoplast', 'Malpica', 'Tecnocard',
       'Compurama', 'Mape', 'Tecnocargo', 'Comunicel', 'Marduk', 'Tecnomuebles', 'Connext', 'Marel', 'TireDirect',
       'Copident', 'MaríaDolores', 'Tractocamiones', 'Crea_Pylsa', 'MartinPacheco', 'TranK', 'CuspideEmp', 'Matec',
       'VRM\ Innovations', 'DLBControl', 'MatecCanada', 'Val_B_Loon', 'Damy', 'MayCard', 'Vegsa', 'Dapesa', 'Mexiled',
       'VictorMarlon', 'Deleites', 'Mhp', 'VisionCare', 'Diseco', 'Mobel', 'Vistabella', 'Dist.XP', 'Modul', 'Vitanova',
       'Divemex', 'Monier', 'as', 'ElRosario', 'Montana', 'aspinet', 'Estatec', 'MovilParts', 'cct', 'Estrasol',
       'Multillantas', 'constantinoramonTecnocor', 'Etytec', 'Nafarrate', 'foxtertools', 'Eurollantas', 'Naresa',
       'isquisa', 'Evolution', 'Natco', 'isquisa2', 'Expormex', 'Nattura', 'metrologiaaplicada', 'FarmaciaZamora',
       'NaturalBioscents', 'nutrimentosquer', 'Fastec', 'NaturalScents_Store', 'pounce', 'FerreteriaTejeda',
       'NaturalTrends', 'scr', 'Ficachi', 'Nestori', 'sistecom', 'Finezza', 'NetOnline(HéctorMagno)', 'sye', 'Franco',
       'Net_Communication', 'tecno', 'G&B', 'Neuroservice']


'''
clientes = []
b = a.split('\t')
c = ' '.join(b)
d = c.split('\n')
e = d[1::]
f = ' '.join(e)
g = f.split(' ')


for x in range(len(g)):
    if g[x] != '':
        clientes.append(g[x])


'''



repo = Repo('/Users/agusquintanar/Desktop/Siil/')
assert not repo.bare

git = repo.git


'''

for cliente in range(186,len(clientes)):
    git.checkout('master')
    git.checkout('HEAD', b= clientes[cliente])
    git.checkout(clientes[cliente])
    os.system('rm -rfv /Users/agusquintanar/Desktop/Siil/Personalizaciones')
    os.system('cp -Rv  /Users/agusquintanar/Desktop/Personalizaciones /Users/agusquintanar/Desktop/Siil/')
    archivos = 'cp -Rv /Volumes/desarr/Desarrollo/Productos/Siil/Clientes/'+ruta_clientes[cliente]+' /Users/agusquintanar/Desktop/Siil/Personalizaciones'
    os.system(archivos)
    read_me_branch = open('Branch_'+clientes[cliente]+'.txt','w')
    read_me_branch.write('Dentro de esta carpeta se encuentran las personalizaciones del cliente: '+clientes[cliente])
    read_me_branch.close()
    os.system('cp -Rv /Users/agusquintanar/Desktop/Final_Fundamenrtos/Branch_'+clientes[cliente]+'.txt /Users/agusquintanar/Desktop/Siil/Personalizaciones')
    repo.git.add(A=True)
    git.commit('-m', 'Creacion de branch para cliente: '+clientes[cliente])

'''
for cliente in range(78,len(clientes)):
    print(clientes[cliente])
    git.push('origin',clientes[cliente])