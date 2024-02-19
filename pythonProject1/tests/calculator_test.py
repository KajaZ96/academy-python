import unittest
from basics.calculator import Calculator

class AdditionTest(unittest.TestCase):



    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_1_plus_1(self):
        self.assertEqual(2,self.calculator.add_values(1,1))

    def test_1_plus_2(self):
        self.assertEqual(3, self.calculator.add_values(1, 2))

    def test_1_plus_string(self):
        self.assertRaises(TypeError, self.calculator.add_values(1, "test"))
    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
