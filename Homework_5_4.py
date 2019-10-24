import unittest
from Homework_5_1 import ITEmployee

class ITEmpolyee_tests(unittest.TestCase):

    def test_fullname(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.full_name, "John Dou")
    def test_birhday(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.birthday, 1975)

    def test_position(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.position, "Analitic")

    def test_exp(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.exp, 1)

    def test_salary(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.salary, 2000)

    def test_sername(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.get_sername(), "Dou")

    def test_name(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.get_name(), "John")

    def test_get_year(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.get_year(), 44)

    def test_up_sal(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        res.up_sal(20)
        self.assertEqual(res.salary, 2020)

    def test_exp_pos(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        self.assertEqual(res.exp_position(), "Junior Analitic")

    def test_skills(self):
        res = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
        res.add_skill("SIEM", "DLP", "CRM")
        self.assertListEqual(res.skills, ["SIEM", "DLP", "CRM"])

    def test_failure(self):
        self.assertRaisesRegex(Exception, "Полное имя должно быть строкой из двух", ITEmployee)

    def test_failure_bithday(self):
        self.assertRaisesRegex(Exception, "Указанна неверная дата рождения", ITEmployee,"John Dou", 1875)

if __name__ == "__main__":
     unittest.main()
