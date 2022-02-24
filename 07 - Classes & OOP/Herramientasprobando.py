from socket import herror


class Herramientas:
    def __init__(self, lista):
        if type(lista)!=list:
            raise TypeError('Elemento ingresado no es una lista')
        else:    
            for i in lista:
                if type(i)!=int:
                    raise ValueError(f'el elemento {i} no es un número entero')
                    break
            self.lista= lista


    def verifica_primo(self):
        lista_clasificacion=[]
        for i in self.lista:
            if self.__verifica_primo(i):
                lista_clasificacion.append((i,True))
            else:
                lista_clasificacion.append((i,False))
        return lista_clasificacion         

    def __verifica_primo(self,numero):
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

    def valor_modal (self,minomax):
        lista_sinrepetir=[]
        for n in self.lista:
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
            while i< len(self.lista):
                if num==self.lista[i]:
                    contador+=1
                i+=1
            repeticiones.append([num,contador])
        num,rep=max(repeticiones, key=lambda item:item[1])        
        return(num)

    def convert_grados(self, med_entrada, med_salida):
        parametros_esperados=['celsius', 'kelvin', 'farenheit']
        if med_entrada.lower() not in parametros_esperados:
            print(med_entrada, 'no es un parámtro esperado. Intente nuevamente con: Celsius, Kelvin o Farenheit')
        elif med_entrada.lower() not in parametros_esperados:
            print(med_entrada, 'no es un parámtro esperado')
        else:    
            for i in self.lista:
                resultado= self.__convert_grados(i, med_entrada,med_salida)
                print(i, 'grados ', med_entrada, 'son ', resultado, 'grados ', med_salida)

    def __convert_grados(self,valor, med_entrada, med_salida):
        med_entrada=med_entrada.lower()
        med_salida=med_salida.lower()
        if (med_entrada==med_salida):
            salida=valor
        elif (med_entrada=='celsius' and med_salida=='farenheit'):
            salida=valor*9/5 + 32
        elif (med_entrada=='celsius' and med_salida=='kelvin'):
            salida=valor+273.15
        elif (med_entrada=='farenheit' and med_salida=="celsius"):
            salida=(valor-32)*5/9
        elif (med_entrada=='kelvin' and med_salida=='celsius'):
            salida= valor-273.15
        elif (med_entrada=='kelvin' and med_salida=='farenheit'):
            grados=self.__convert_grados(valor,'kelvin','celsius')
            salida=self.__convert_grados(grados,'celsius','farenheit')
        elif (med_entrada=='Farenheit' and med_salida=='kelvin'):
            grados=self.__convert_grados(valor,'farenheit','celsius')
            salida=self.__convert_grados(grados,'celsius','kelvin')
        return(salida)

    def factorial(self):
        lista_factorial=[]
        for i in self.lista:
            resultado=self.__factorial(i)
            lista_factorial.append((i,resultado ))
        return(lista_factorial)
            
    def __factorial(self,num):
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


param=[1,2,3,4,5,6,7]
resultado=[False,True,True,False,True,False,True]
h=Herramientas(param)
prueba= h.verifica_primo()

print(h.convert_grados.locals())



