import unittest
from app import create_app, db
from app.config import TestConfig
from app.models import Producto

class TestInsertar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.ctx = cls.app.app_context()
        cls.ctx.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.ctx.pop()

    def test_insertar_producto(self):

        producto = Producto(
            nombre="Producto Test",
            precio=100,
            stock=5
        )

        db.session.add(producto)
        db.session.commit()

        consulta = Producto.query.filter_by(
            nombre="Producto Test"
        ).first()

        self.assertIsNotNone(consulta)

        db.session.delete(consulta)
        db.session.commit()

if __name__ == "__main__":
    unittest.main()