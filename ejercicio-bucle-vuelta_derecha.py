# coding: utf8
# Adrià Salvadó
# Inicializaciones
salir = "N"
inicio=1
maximo=8

while ( salir=="N" ):
    # Hago cosas
    if(inicio%8==1) or (inicio%8==2):
		print inicio, "-> Arriba"
    if(inicio%8==3) or (inicio%8==4):
		print inicio, "-> Derecha"
    if(inicio%8==5) or (inicio%8==6):
		print inicio,"-> Abajo"
    if(inicio%8==7) or (inicio%8==0):
		print inicio, "-> Izquierda"

    # Incremento
    inicio=inicio+1
    # Activo indicador de salida si toca
    if ( inicio > maximo ): # Condición de salida
            salir = "S"
