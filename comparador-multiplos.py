# coding: utf8
# Adrià Salvadó

num1=input("Escribe un numero: ")
num2=input("Escribe un numero: ")

if(num1==0) or (num2==0):
	print "No puede ser 0"

else:
	if(num1>num2):
		mayor=num1
		menor=num2
	
	else: 
		mayor=num2
		menor=num1
		
	if(mayor%menor==0):
		print mayor, "es multiplo de" ,menor
	
	else:
		print mayor, "no es multiplo de" ,menor
