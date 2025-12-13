import unittest


def teszt_eset():
    def add(a, b):
        return a + b

    class TestMathOperatios(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 1), 0)
            self.assertNotEqual(add(2, 3), 6)


def try_catch():
    def divide(a, b):
        if b == 0:
            raise ValueError("0val nem lehet osztani")
        return a / b

    class TestDivide(unittest.TestCase):
        def test_divide_by_zero(self):
            with self.assertRaises(ValueError):
                divide(10, 0)



def test_2_class_func():
    class TestA(unittest.TestCase):
        def test_case_1(self):
            self.assertTrue(True)

    class TestB(unittest.TestCase):
        def test_case_2(self):
            self.assertFalse(False)

    suite = unittest.TestSuite()

    suite.addTest(TestA('test_case1'))
    suite.addTest(TestB('test_case2'))

    runner = unittest.TextTestRunner()
    runner.run(suite)