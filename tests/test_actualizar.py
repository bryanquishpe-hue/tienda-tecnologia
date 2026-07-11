import unittest
from app import create_app, db
from app.config import TestConfig
from app.models import Producto

class TestActualizar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.ctx = cls.app.app_context()
        cls.ctx.push()
        db.create_all()

        producto = Producto(nombre="Producto Test", precio=100, stock=5)
        db.session.add(producto)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.ctx.pop()

    def test_actualizar_stock(self):

        producto = Producto.query.first()

        self.assertIsNotNone(producto)

        stock_anterior = producto.stock

        producto.stock = stock_anterior + 1

        db.session.commit()

        actualizado = db.session.get(Producto, producto.id)

        self.assertEqual(
            actualizado.stock,
            stock_anterior + 1
        )

        actualizado.stock = stock_anterior

        db.session.commit()

if __name__ == "__main__":
    unittest.main()