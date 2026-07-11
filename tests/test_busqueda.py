import unittest
from app import create_app
from app.models import Producto

class TestBusqueda(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

    @classmethod
    def tearDownClass(cls):
        cls.ctx.pop()

    def test_busqueda(self):

        productos = Producto.query.filter(
            Producto.nombre.like("%Laptop%")
        ).all()

        self.assertGreaterEqual(len(productos), 1)

if __name__ == "__main__":
    unittest.main()