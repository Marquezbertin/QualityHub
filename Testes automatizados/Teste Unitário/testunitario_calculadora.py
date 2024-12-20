import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    """
    Classe de testes unitários para a classe Calculadora.
    """

    def setUp(self):
        """
        Método executado antes de cada teste. Cria uma instância da Calculadora.
        """
        self.calc = Calculadora()

    def test_adicionar(self):
        """
        Testa o método adicionar.
        """
        self.assertEqual(self.calc.adicionar(2, 3), 5)
        self.assertEqual(self.calc.adicionar(-1, 1), 0)
        self.assertEqual(self.calc.adicionar(-1, -1), -2)

    def test_subtrair(self):
        """
        Testa o método subtrair.
        """
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(-1, 1), -2)
        self.assertEqual(self.calc.subtrair(-1, -1), 0)

    def test_multiplicar(self):
        """
        Testa o método multiplicar.
        """
        self.assertEqual(self.calc.multiplicar(3, 7), 21)
        self.assertEqual(self.calc.multiplicar(-1, 1), -1)
        self.assertEqual(self.calc.multiplicar(-1, -1), 1)

    def test_dividir(self):
        """
        Testa o método dividir.
        """
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-1, 1), -1)
        self.assertEqual(self.calc.dividir(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()