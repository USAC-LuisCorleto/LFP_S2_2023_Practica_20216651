from Inventario import Invent

inventario = Invent()

while True:
    print("-------------------------")
    print("| SISTEMA DE INVENTARIO |")
    print("-------------------------")
    print("[1]. Cargar inventario inicial")
    print("[2]. Cargar instrucciones de movimientos")
    print("[3]. Crear informe de inventario")
    print("[4]. Salir")
    print("[5]. Imprimir")

    opcionMen = input("Seleccione una opción: ")

    #Cargando inventario inicial.
    if opcionMen == "1":
        print("-----------------------------")
        print("| CARGAR INVENTARIO INICIAL |")
        print("-----------------------------")
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        productos_cargados = inventario.leer_archivo(nombreArchivo)
        if productos_cargados:
            print(f"-El archivo {nombreArchivo} fue cargado correctamente.-")
        else:
            print(f"-Hubo un problema al cargar el archivo {nombreArchivo}.-")

    #Cargando archivo de instrucciones.
    if opcionMen == "2":
        print("---------------------------------------")
        print("| CARGAR INSTRUCCIONES DE MOVIMIENTOS |")
        print("---------------------------------------")
        nombreArchivoMovs = input("Ingrese el nombre del archivo de instrucciones: ")
        movimientos_leidos = inventario.leer_instrucciones(nombreArchivoMovs)
        if movimientos_leidos:
            print(f"-El archivo {nombreArchivoMovs} fue leído correctamente.-")
        else:
            print("Este punto se alcanza pero movimientos_leidos es False.")

    #Creación de informe de inventario.
    if opcionMen == "3":
        print("------------------------------")
        print("| CREAR INFORME DE INVENTARIO")
        print("------------------------------")

    if opcionMen == "4":
        print("Saliendo...")
        break
    
    #Verificación de los movimientos.
    if opcionMen == "5":
        print("\n")
        print("-------------------------")
        inventario.imprimir_inventario()