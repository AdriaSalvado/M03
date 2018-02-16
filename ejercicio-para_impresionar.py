# coding: utf8
# Adrià Salvadó

edad1=input("Introduce la edad del chico: ")
edad2=input("Introduce la edad de la chica: ")
    
if(edad1==edad2):
	if(edad1%2==0) and (edad2%2==0):
		print "Tienen la misma edad par"	
	
	else:
		if(edad1%2!=0) and (edad2%2!=0):
			print "Tienen la misma edad inpar"


if(edad1>edad2):
		print "El chico es mayor que la chica"
		if(edad1>=18) and (edad2<18):
		    print "El chico es mayor de edad y la chica es menor"
		
		else:
			if(edad1<18):
				print "Los dos son menores de edad pero el chico es mayor que la chica"
else:
	print "La chica es mayor"
	if(edad2>=18) and (edad1<18):
		print "La chica es mayor de edad y el chico es menor"
	
	else:
		if(edad2<18):
			print "Los dos son menores de edad pero la chica es mayor que el chico"			
