import unittest
from app import somar


class TestApp(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -2), -3)


if __name__ == "__main__":
    unittest.main()