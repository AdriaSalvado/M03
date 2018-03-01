# coding: utf8
# Adrià Salvadó
import os
os.system("clear")
from math import pi
print """
╔═══════════════════════════════════════╗
║ a) Triángulo                          ║
║ b) Círculo                            ║                              
║                                       ║                                       
╚═══════════════════════════════════════╝
"""
forma=raw_input("Elije una forma (t/c): ")
forma=forma.upper()
if(forma=="T"):
	base=input("Escriba la base: ")
	altura=input("Escriba la altura: ")
	if(base<0) or (altura<0):
		print "ERROR no se pueden negativos"
	else:
		print "Un tiángulo de base" ,base, "y altura" ,altura, "tiene una área de" ,(base*altura)/2,
else:
    if(forma=="C"):
        radio=input("Escriba el radio: ")
        if(radio<0):
            print "ERROR no se pueden negativos"
        else:
            print "Un círculo de radio" ,radio, "tiene un área de" ,round(pi*radio*2,2)
    else:
		print "Tiene que ser t o c"
