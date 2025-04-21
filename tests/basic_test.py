# testing/tests/basic_test.py

import unittest
import testing


class TestObject(unittest.TestCase):
    def test_get_name(self):
        name = "name"
        tmp_obj = testing.Object(name)
        self.assertEqual(tmp_obj.get_name(), name)
    
    def test_adding(self):
        num1 = 5
        num2 = -5
        total = 0
        self.assertEqual(testing.adding(num1, num2), total)


if __name__ == "__main__":
    unittest.main()
