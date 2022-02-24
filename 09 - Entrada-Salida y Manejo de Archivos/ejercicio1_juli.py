Edad= input('¿Qué edad tienes? ')
Color=input('¿Cuál es tu color favorito? ')
Pais=input('¿Cuál es su país de referencia? ')

import sys

if len(sys.argv)==4:
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
else:
    (print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)"))

