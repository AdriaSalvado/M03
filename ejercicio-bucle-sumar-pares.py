# coding: utf8
# Adrià Salvadó
# Inicializaciones

salir = "N"
suma=1
resultado=0

while ( salir=="N" ):
    # Hago cosas
    if(resultado%2==0):
		print resultado

    # Incremento
    resultado=resultado + suma
    suma=suma+1
    # Activo indicador de salida si toca
    if ( resultado > 15): # Condición de salida
            salir = "S"
