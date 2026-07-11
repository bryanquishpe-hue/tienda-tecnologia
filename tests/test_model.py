import unittest
from app import create_app, db
from app.config import TestConfig
from app.models import Producto

class TestProducto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.ctx = cls.app.app_context()
        cls.ctx.push()
        db.create_all()

        producto = Producto(nombre="Laptop de prueba", precio=100, stock=5)
        db.session.add(producto)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.ctx.pop()

    def test_existen_productos(self):
        productos = Producto.query.all()
        self.assertGreater(len(productos), 0)

if __name__ == "__main__":
    unittest.main()