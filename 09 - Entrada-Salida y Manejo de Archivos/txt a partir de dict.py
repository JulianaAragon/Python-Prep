montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

tabla=[]
elementos=list(montañas.values())
for i in range(len(elementos[0])):
        tabla.append([])
        for j in range(len(montañas.keys())):
            tabla[i].append(elementos[j][i])

n=len(elementos[0])


claves=montañas.keys()


tabla_str=[]
for i in range(len(tabla)):
        fila=",".join(map(str,tabla[i]))
        tabla_str.append(fila)
fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila8,fila9,fila10=tabla_str

#creo archivo de texto y lo modifico
import os
archivo_texto=open('clase09_ej3.csv','w')

archivo_texto.write(",".join(map(str,claves))+'\n')

for i in tabla_str:
    archivo_texto.write(i+'\n')

archivo_texto.write(tabla_str[9])

archivo_texto.close()