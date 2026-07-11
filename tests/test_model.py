import unittest
from app import create_app
from app.models import Producto

class TestProducto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

    @classmethod
    def tearDownClass(cls):
        cls.ctx.pop()

    def test_existen_productos(self):
        productos = Producto.query.all()
        self.assertGreater(len(productos), 0)

if __name__ == "__main__":
    unittest.main()