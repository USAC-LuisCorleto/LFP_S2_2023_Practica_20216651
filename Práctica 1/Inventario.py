from Producto import Product

class Invent:
    def __init__(self):
        self.productos = []

    def leer_archivo(self, nombre_archivo):
        self.productos = []
        try:
            with open(nombre_archivo, 'r') as archivo:
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

    def imprimir_inventario(self):
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Cantidad:", producto.cantidad)
            print("Precio Unitario:", producto.precioUni)
            print("Ubicación:", producto.ubicacion)
            print("-------------------------")