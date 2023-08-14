from Producto import Product

class Invent:
    def __init__(self):
        self.productos = []

    #Función para leer el primero archivo en la creación del inventario.
    def leer_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()

            for linea in lineas:
                if linea.startswith("crear_producto "):
                    partes = linea.strip().split(" ")[1].split(";") 
                    if len(partes) == 4:
                        nombre, cantidad, precioUni, ubicacion = partes
                        producto = Product(nombre, int(cantidad), float(precioUni), ubicacion)
                        self.productos.append(producto)
                    else:
                        print(f"Error en la línea: {linea.strip()}")
            return self.productos
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        except Exception as e:
            print("Ocurrió un error:", e)

    #Función para leer el archivo e identificar cada instrucción.
    def leer_instrucciones(self, nombre_archivo):
        número = 0
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()

            for linea in lineas:
                número+=1
                print(f"Procesando línea:, {número} {linea}")
                if linea.startswith("agregar_stock "):
                    partes = linea.strip().split(" ")[1].split(";")
                    if len(partes) == 3:
                        nombre, cantidad, ubicacion = partes
                        #print(f"Intentando agregar stock de {cantidad} unidades de '{nombre}' en '{ubicacion}'")
                        self.agregar_stock(nombre, int(cantidad), ubicacion)

                if linea.startswith("vender_producto "):
                    partes = linea.strip().split(" ")[1].split(";")
                    if len(partes) == 3:
                        nombre, cantidad, ubicacion = partes
                        #print(f"Intentando vender {cantidad} unidades de '{nombre}' en '{ubicacion}'")
                        self.vender_producto(nombre, int(cantidad), ubicacion)
            return True
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        except Exception as e:
            print("Ocurrió un error:", e)
        return False

    #Método para la venta de productos.
    def vender_producto(self, nombre_producto, cantidad, ubicacion):
        producto_encontrado = None

        for producto in self.productos:
            if producto.nombre == nombre_producto and producto.ubicacion == ubicacion:
                producto_encontrado = producto
                break
            
        if producto_encontrado is None:
            print(f"No se encontró el producto {nombre_producto} en la ubicación {ubicacion}")
            return
        if producto_encontrado.cantidad < cantidad:
            print(f"No hay suficiente cantidad de {nombre_producto} en la ubicación {ubicacion}")
            return
        producto_encontrado.cantidad -= cantidad
        print(f"Se vendieron {cantidad} unidades de {nombre_producto} en la ubicación {ubicacion}")

    #Método para agregar productos al inventario.
    def agregar_stock(self, nombre_producto, cantidad, ubicacion):
        producto_encontrado = None

        for producto in self.productos:
            if producto.nombre == nombre_producto and producto.ubicacion == ubicacion:
                producto_encontrado = producto
                break
        if producto_encontrado is None:
            print(f"No se encontró el producto '{nombre_producto}' en la ubicación '{ubicacion}'. No se puede agregar stock.")
            return
        producto_encontrado.cantidad += cantidad
        print(f"Se agregaron {cantidad} unidades de '{nombre_producto}' en la ubicación '{ubicacion}'.")

    #Impresión del inventario.
    def imprimir_inventario(self):
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Cantidad:", producto.cantidad)
            print("Precio Unitario:", producto.precioUni)
            print("Ubicación:", producto.ubicacion)
            print("-------------------------")