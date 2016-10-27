lista=[] 
sinpar = 0
sacados = 0
cont = 1
cadena = ""

def llenarLista():
	archivo = open("movies.txt")
	while True:
	    linea=archivo.readline()[:-1]       
	    if not linea: break
	    lista.append(linea.replace(' ', ''))
	archivo.close()
    
def concatenaPeliculas():
	lista.reverse()

	aux = len(lista)

	global cont
	global sinpar
	global cadena
	global sacados
	global vuleta

	while True:

		a = lista[0]
		b = lista[cont]
		
		if (a[len(a)-1]) == b[0].lower(): 
			cadena += a		
			lista[0] = lista.pop(cont)
			sacados += 1
			cont = 1
			#print cadena			
		else:
			cont +=1		
			if (cont == len(lista)):
				if (sinpar == aux):
					return cadena							
				lista.append(lista.pop(0))			
				cont = 1
				sinpar += 1
def main():	
	llenarLista()
	cadenas = concatenaPeliculas()
	print cadenas
	print ("")
	print ("El numero de peliculas unidas es: "  + str(sacados))
	print "El tamano de tu cadena es: " + str(len(cadena))
	print ("El remanente es de: "+ str(len(lista)))
	print ("")
	print lista


if __name__ == "__main__":
    main()

