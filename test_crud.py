# test_crud.py
import unittest
from main import Producto, CRUDProductos

class TestCRUDProductos(unittest.TestCase):
    def setUp(self):
        self.crud = CRUDProductos()
        self.producto1 = Producto(1, "Producto1", "Descripción1", 100.0, 10)
        self.producto2 = Producto(2, "Producto2", "Descripción2", 200.0, 20)
        self.crud.crear_producto(self.producto1)

    def test_crear_producto_exitoso(self):
        self.crud.crear_producto(self.producto2)
        self.assertEqual(len(self.crud.productos), 2)

    def test_crear_producto_duplicado(self):
        with self.assertRaises(ValueError):
            self.crud.crear_producto(self.producto1)

    def test_leer_producto_exitoso(self):
        producto = self.crud.leer_producto(1)
        self.assertEqual(producto, self.producto1)

    def test_leer_producto_no_existente(self):
        with self.assertRaises(ValueError):
            self.crud.leer_producto(3)

    def test_actualizar_producto_exitoso(self):
        self.crud.actualizar_producto(1, nombre="NuevoNombre")
        self.assertEqual(self.producto1.nombre, "NuevoNombre")

    def test_actualizar_producto_no_existente(self):
        with self.assertRaises(ValueError):
            self.crud.actualizar_producto(3, nombre="Inexistente")

    def test_eliminar_producto_exitoso(self):
        self.crud.eliminar_producto(1)
        self.assertEqual(len(self.crud.productos), 0)

    def test_eliminar_producto_no_existente(self):
        with self.assertRaises(ValueError):
            self.crud.eliminar_producto(3)

if __name__ == "__main__":
    unittest.main()
