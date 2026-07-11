import unittest
from app import create_app
from app import db

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def test_conexion_bd(self):
        resultado = db.session.execute(db.text("SELECT 1"))
        self.assertEqual(resultado.scalar(), 1)

if __name__ == "__main__":
    unittest.main()