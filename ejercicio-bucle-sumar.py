# coding: utf8
# Adrià Salvadó
# Inicializaciones

salir = "N"
inicio=1
final=input("Introduce el numero final: ")
suma=0

if(final<=0):
	print "Error no puede ser cero"

while ( salir=="N" ):
    # Hago cosas
    print inicio

    # Incremento
    suma=inicio + suma
    inicio=suma+1
    # Activo indicador de salida si toca
    if ( suma > final ): # Condición de salida
            salir = "S"
