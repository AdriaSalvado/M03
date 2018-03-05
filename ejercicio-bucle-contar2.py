# coding: utf8
# Inicializaciones
salir = "N"
numero=1
numero1=input("Introduce el numero limite: ")

if(numero1<=0):
	salir=="S"
while ( salir=="N" ):
    # Hago cosas
    print numero

    # Incremento
    numero = numero +1
    # Activo indicador de salida si toca
    if ( numero > numero1 ): # Condición de salida
        salir = "S"

  
