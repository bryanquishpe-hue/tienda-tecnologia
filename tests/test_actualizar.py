import unittest
from app import create_app, db
from app.models import Producto

class TestActualizar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

    @classmethod
    def tearDownClass(cls):
        cls.ctx.pop()

    def test_actualizar_stock(self):

        producto = Producto.query.first()

        self.assertIsNotNone(producto)

        stock_anterior = producto.stock

        producto.stock = stock_anterior + 1

        db.session.commit()

        actualizado = Producto.query.get(producto.id)

        self.assertEqual(
            actualizado.stock,
            stock_anterior + 1
        )

        actualizado.stock = stock_anterior

        db.session.commit()

if __name__ == "__main__":
    unittest.main()