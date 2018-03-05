# coding: utf8
# Inicializaciones
salir = "N"
anyo= 2010

while ( salir=="N" ):
    # Hago cosas
    print "Informes del año" ,anyo

    # Incremento
    anyo = anyo + 1
    # Activo indicador de salida si toca
    if ( anyo > 2016 ): # Condición de salida
            salir = "S"
