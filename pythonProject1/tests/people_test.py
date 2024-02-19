import unittest

from basics.classes import Student
class AdditionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Jan", "Jan", 1999, [2, 2])

    def test_grades(self):
        self.assertEqual(2, self.student.calculate_average())
        self.student.add_grade(4)
        self.student.add_grade(5)
        self.assertEqual(3, self.student.calculate_average())


if __name__ == '__main__':
    unittest.main()
