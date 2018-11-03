'''11-3 雇员'''
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.don = Employee('don', 'hu', 65000)

    def test_give_default_raise(self):
        self.don.give_raise()
        self.assertEqual(self.don.salary, 70000)

    def test_give_custom_raise(self):
        self.don.give_raise(10000)
        self.assertEqual(self.don.salary, 75000)

unittest.main()