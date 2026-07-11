import unittest
from app import create_app, db
from app.config import TestConfig
from app.models import Producto

class TestEliminar(unittest.TestCase):

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

    def test_eliminar_producto(self):

        producto = Producto(
            nombre="Eliminar Test",
            precio=10,
            stock=1
        )

        db.session.add(producto)
        db.session.commit()

        id_producto = producto.id

        db.session.delete(producto)
        db.session.commit()

        consulta = db.session.get(Producto, id_producto)

        self.assertIsNone(consulta)

if __name__ == "__main__":
    unittest.main()