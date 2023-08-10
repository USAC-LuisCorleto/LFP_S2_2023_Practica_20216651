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

    if opcionMen == "1":
        print("-----------------------------")
        print("| CARGAR INVENTARIO INICIAL |")
        print("-----------------------------")
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        if inventario.leer_archivo(nombreArchivo):
            print(f"-El archivo {nombreArchivo} fue cargado correctamente.-")
        else:
            print(f"-Hubo un problema al cargar el archivo {nombreArchivo}.-")

    if opcionMen == "2":
        print("---------------------------------------")
        print("| CARGAR INSTRUCCIONES DE MOVIMIENTOS |")
        print("---------------------------------------")

    if opcionMen == "3":
        print("------------------------------")
        print("| CREAR INFORME DE INVENTARIO")
        print("------------------------------")

    if opcionMen == "4":
        print("Saliendo...")
        break

    if opcionMen == "5":
        print("\n")
        print("-------------------------")
        inventario.imprimir_inventario()