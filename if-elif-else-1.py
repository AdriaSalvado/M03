# coding: utf8
# Adrià Salvadó

dividendo=input ("Escriba el dividendo: ")
divisor=input ("Escriba el divisor: ")



if (divisor==0):
	print "No se puede dividir entre 0"

else:
    if(resto==0):
		print "La division es exacta. Cociente:" , dividendo/divisor 

    else: 
        print "La division no es exacta. Cociente:" , dividendo/divisor , "Resto:" ,dividendo%divisor
