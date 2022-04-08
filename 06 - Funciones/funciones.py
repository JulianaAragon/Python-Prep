def num_primo (numero):
    status=False
    if numero==0 or numero==1:
        status=False
    if numero==2:
        status=True
    
    else:
        for divisor in range(2,numero):
            if numero%divisor==0:
                status=False
                break
                
            status=True
    return(status)


def num_repetidos (lista,minomax):
    lista_sinrepetir=[]
    for n in lista:
        if n not in lista_sinrepetir:
            lista_sinrepetir.append(n)
    if minomax=='min':
        lista_sinrepetir.sort()
    elif minomax=='max':
        lista_sinrepetir.reverse()
    repeticiones=[]
    for num in lista_sinrepetir:
        i=0
        contador=0
        while i< len(lista):
            if num==lista[i]:
                contador+=1
            i+=1

        repeticiones.append([num,contador])
    num,rep=max(repeticiones, key=lambda item:item[1])        
    return(num)

def convert_grados (valor, med_entrada, med_salida):
    if (med_entrada==med_salida):
        salida=valor
    elif (med_entrada=='Ce' and med_salida=='Fa'):
        salida=valor*9/5 + 32
    elif (med_entrada=='Ce' and med_salida=='Ke'):
        salida=valor+273.15
    elif (med_entrada=='Fa' and med_salida=="Ce"):
        salida=(valor-32)*5/9
    elif (med_entrada=='Ke' and med_salida=='Ce'):
        salida= valor-273.15
    elif (med_entrada=='Ke' and med_salida=='Fa'):
        grados=convert_grados(valor,'Ke','Ce')
        salida=convert_grados(grados,'Ce','Fa')
    elif (med_entrada=='Fa' and med_salida=='Ke'):
        grados=convert_grados(valor,'Fa','Ce')
        salida=convert_grados(grados,'Ce','Ke')
    return(salida) 

def factorial(num):
    if (num<0 or type(num)==float):
        salida='Número no entero o negativo'
    elif num==0:
        salida=1
    else:
        factor=1
        for i in range(2,num+1):
            factor*=i
        salida=factor
    
    return(salida)
    
print(factorial(5))