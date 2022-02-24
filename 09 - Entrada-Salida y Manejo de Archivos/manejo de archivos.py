from io import open

#crear archivo
archivo_texto=open('archivo.txt','w')

frase='Estupendo día para estudiar Python \n el miércoles'

archivo_texto.write(frase)
archivo_texto.close() #siempre hay que cerrar

#leer lo que hay en el archivo y almacenar en variable

archivo_texto=open('archivo.txt','r')
texto=archivo_texto.read()
archivo_texto.close() 

print(texto)

#leer lo que hay en el archivo y almacenar cada línea de texto en una lsta

archivo_texto=open('archivo.txt','r')
lineas_texto=archivo_texto.readlines()
archivo_texto.close() 

print(lineas_texto)

#agregar lineas

archivo_texto=open('archivo.txt','a')
archivo_texto.write('\n siempre es una buena ocasión para estudiar')
archivo_texto.close()

#modificar posición del puntero
archivo_texto=open('archivo.txt','r')
print(archivo_texto.read()) #termina de lleer y cursor queda al final

archivo_texto.seek(0) #vuelvo a situar el cursor en posición inicial
print(archivo_texto.read(11)) #lee hasta posición 11

#agregar linea
archivo_texto=open('archivo.txt','r+')
lineas_texto=archivo_texto.readlines()
lineas_texto[1]='Texto agregado \n'
archivo_texto.seek(0)
archivo_texto.writelines(lineas_texto)
archivo_texto.close()
