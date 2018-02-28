# coding: utf8
# Adrià Salvadó

import os

os.system ("clear")
print """
╔═══════════════════════════════════════╗
║                                       ║
║     Calculador de años bisiestos      ║                              
║                                       ║                                       
╚═══════════════════════════════════════╝
"""
anio=input("Introduce un año: ")

if(anio<=0):
    print "No puede ser ni cero ni un año negativo"

else:
    if(anio%4==0) and (400%anio==0):
        print "El año" ,anio, "es bisiesto"
    elif(anio%100!=0):
		print "El año" ,anio, "no es bisiesto"
        

