import unittest
from app import create_app, db
from app.models import Producto

class TestEliminar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

    @classmethod
    def tearDownClass(cls):
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

        consulta = Producto.query.get(id_producto)

        self.assertIsNone(consulta)

if __name__ == "__main__":
    unittest.main()