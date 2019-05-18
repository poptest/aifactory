import unittest
from jiawei.db.calcultor import Calcultor

class TestCalcultor(unittest.TestCase):
    def test_jian(self):
        a=5
        b=2
        act_ret=Calcultor.jian(a ,b)
        exp_ret=3
        self.assertEqual(exp_ret, act_ret)


if __name__ == '__main__':
    unittest.main()
