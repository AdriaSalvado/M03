# coding: utf8
# Inicializaciones
salir = "N"
numero=2
numero1=input("Introduce el numero limite: ")

if(numero1<=1):
	salir=="S"
else:
	while ( salir=="N" ):
    # Hago cosas
		print numero

    # Incremento
		numero = numero +2
    # Activo indicador de salida si toca
		if ( numero > numero1 ): # Condición de salida
			salir = "S"

  
