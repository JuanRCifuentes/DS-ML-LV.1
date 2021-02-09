import unittest

def sum(num_1, num_2):
    return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):

    def test_sum(self):
        num_1 = 10
        num_2 = 5

        resultado = sum(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_sum_negatives(self):
        num_1 = -10
        num_2 = -7

        resultado = sum(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()