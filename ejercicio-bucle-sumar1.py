# coding: utf8
# Inicializaciones
# Adrià Salvadó
salir = "N"
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    # Hago cosas
    print numero 
   
	
    suma=suma+numero
    # Incremento
    numero=numero+1
    # Activo indicador de salida si toca
    if ( numero > maximo ): # Condición de salida
            salir = "S"
print "=" , suma 
