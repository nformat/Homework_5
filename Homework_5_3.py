import unittest
from Homework_3_6 import is_year_leap, tre, tretype


class Is_year_leap_Tests(unittest.TestCase):

    def test_istrue(self):
        res = is_year_leap(2000)
        self.assertTrue(res, True)


    def test_isnottrue(self):
        res = is_year_leap(2001)
        self.assertFalse(res, False)


    def test_isnotnone(self):
        res = is_year_leap(2001)
        self.assertIsNotNone(res, True)


    def test_failure(self):
        self.assertRaises(Exception, is_year_leap)


class Tre_tests(unittest.TestCase):


    def test_zero(self):
        res = tre(0, 0, 0)
        self.assertFalse(res, False)


    def test_false(self):
        res = tre(1, 3, 1)
        self.assertFalse(res, False)


    def test_true(self):
        res= tre(2, 3, 2)
        self.assertTrue(res, True)


    def test_isnotnone(self):
        res = tre(1, 3, 1)
        self.assertIsNotNone(res, True)


    def test_failure(self):
        self.assertRaisesRegex(Exception, "missing 2 required positional arguments:", tre, 1)


    def test_failure_2(self):
        self.assertRaisesRegex(Exception, "missing 1 required positional argument:", tre, 1, 3)



class Tretype_tests(unittest.TestCase):


    def test_zero(self):
        res = tretype(0, 0, 0)
        self.assertEquals(res, "несуществует")


    def test_type1(self):
        res = tretype(2, 2, 2)
        self.assertEquals(res, "равносторний")

    def test_type2(self):
        res = tretype(2, 3, 2)
        self.assertEquals(res, "равнобедренный")


    def test_type3(self):
        res = tretype(2, 3, 4)
        self.assertEquals(res, "разностороний")


    def test_isnotnone(self):
        res = tre(1, 3, 1)
        self.assertIsNotNone(res, True)


    def test_failure(self):
        self.assertRaisesRegex(Exception, " missing 2 required positional arguments:", tre, 1)


    def test_failure_2(self):
        self.assertRaisesRegex(Exception, "missing 1 required positional argument:", tre, 1, 3)


if __name__ == "__main__":
     unittest.main()
