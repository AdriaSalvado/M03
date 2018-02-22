# coding: utf8
# Adrià Salvadó
import os

os.system ("clear")

print"""	
#####################################################################
#                    #                     #                        #
# -Super             # -Sin plomo          # -Diesel                #
#  Normal 1.5€  = 1  #  Normal 1.6€    = 3 #  Normal 1.7€       = 5 #
#  Turbo  1.55€ = 2  #  Aditivos 1.66€ = 4 #  Fast&Furius 1.77€ = 6 #
#                    #                     #                        #
##################################################################### 
"""		
gasolina=input("Que tipo de gasolina quiere? ")		

		
if(gasolina<=0) or (gasolina >=7):
	print "Numero de gasolina o de litros no compatible"

elif(gasolina==1):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Super-Normal" , litros , "Litros. Precio:" ,1.5*litros, "€"		

elif(gasolina==2):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Super-Normal" , litros , "Litros. Precio:" ,1.55*litros, "€"	

elif(gasolina==3):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Sin plomo-Normal" , litros , "Litros. Precio:" ,1.6*litros, "€"	

elif(gasolina==4):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Sin plomo-Aditivos" , litros , "Litros. Precio:" ,1.65*litros, "€"	

elif(gasolina==5):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Diesel-Normal" , litros , "Litros. Precio:" ,1.7*litros, "€"	

elif(gasolina==6):
	litros=input("Cuantos litros de gasolina quiere? ")
	print "Gasolina Diesel-Fast&Furius" , litros , "Litros. Precio:" ,1.75*litros, "€"		
