#Ejercicio 1

from timeit import default_timer

def busquedaBinaria(unaLista, item):  
	    primero = 0
	    ultimo = len(unaLista)-1
	    encontrado = False
	    while primero <= ultimo and not encontrado:
	        puntoMedio = (primero + ultimo)//2 #Division entera 
	        if unaLista[puntoMedio] == item:
	            encontrado = True
	        else:
	            if item < unaLista[puntoMedio]:
	                ultimo = puntoMedio-1
	            else:
	                primero = puntoMedio+1
	
	    return encontrado
	
listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

inicio = default_timer()
busquedaBinaria(listaPrueba, 0)
fin = default_timer()
print(fin - inicio)
print()
inicio = default_timer()
busquedaBinaria(listaPrueba, 13)
fin = default_timer()
print(fin - inicio)
print()
inicio = default_timer()
busquedaBinaria(listaPrueba, 42)
fin = default_timer()

print(fin - inicio)