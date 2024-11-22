
class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, descripcion={self.descripcion}, precio={self.precio}, cantidad={self.cantidad})"



import json
import os

class CRUDProductos:
    def __init__(self, data_file='data/productos.json'):
        self.data_file = data_file
        self.productos = []
        self._cargar_productos()

    def _cargar_productos(self):
        """Carga los productos desde el archivo JSON, si existe."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                productos_data = json.load(file)
                self.productos = [Producto(**p) for p in productos_data]
        else:
            self.productos = []

    def _guardar_productos(self):
        """Guarda los productos en el archivo JSON."""
        with open(self.data_file, 'w') as file:
            productos_data = [p.__dict__ for p in self.productos]
            json.dump(productos_data, file, indent=4)

    def crear_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            raise ValueError(f"El producto con ID {producto.id} ya existe.")
        self.productos.append(producto)
        self._guardar_productos()

    def leer_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        raise ValueError(f"No se encontró un producto con ID {id}.")

    def actualizar_producto(self, id, nombre=None, descripcion=None, precio=None, cantidad=None):
        producto = self.leer_producto(id)
        if nombre:
            producto.nombre = nombre
        if descripcion:
            producto.descripcion = descripcion
        if precio:
            producto.precio = precio
        if cantidad:
            producto.cantidad = cantidad
        self._guardar_productos()

    def eliminar_producto(self, id):
        producto = self.leer_producto(id)
        self.productos.remove(producto)
        self._guardar_productos()


def main():
    crud = CRUDProductos()
    
    while True:
        print("\n--- CRUD Productos ---")
        print("1. Crear Producto")
        print("2. Leer Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            try:
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = Producto(id, nombre, descripcion, precio, cantidad)
                crud.crear_producto(producto)
                print("Producto creado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == "2":
            try:
                id = int(input("ID del producto a leer: "))
                producto = crud.leer_producto(id)
                print(f"Producto encontrado: {producto}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == "3":
            try:
                id = int(input("ID del producto a actualizar: "))
                nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
                precio = input("Nuevo precio (dejar vacío para no cambiar): ")
                cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")

                crud.actualizar_producto(
                    id,
                    nombre=nombre or None,
                    descripcion=descripcion or None,
                    precio=float(precio) if precio else None,
                    cantidad=int(cantidad) if cantidad else None
                )
                print("Producto actualizado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == "4":
            try:
                id = int(input("ID del producto a eliminar: "))
                crud.eliminar_producto(id)
                print("Producto eliminado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

