import unittest

import calc


class TestCalc(unittest.TestCase):

    def test_divide(self):
        result = calc.divide(15, 5)
        self.assertEqual(result, 3)

        with self.assertRaises(ValueError):
            calc.divide(15, 0)

    def test_add(self):
        result = calc.add(15, 5)
        self.assertEqual(result, 20)

    def test_multiply(self):
        result = calc.multiply(15, 5)
        self.assertEqual(result, 75)


if __name__ == '__main__':
    unittest.main()
