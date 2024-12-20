class Calculadora:
    """
    Classe Calculadora para realizar operações aritméticas básicas.
    """

    def adicionar(self, a, b):
        """
        Retorna a soma de dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Soma de a e b
        """
        return a + b

    def subtrair(self, a, b):
        """
        Retorna a subtração de dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Subtração de a e b
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Retorna a multiplicação de dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Multiplicação de a e b
        """
        return a * b

    def dividir(self, a, b):
        """
        Retorna a divisão de dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Divisão de a por b
        :raises ValueError: Se b for zero
        """
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b