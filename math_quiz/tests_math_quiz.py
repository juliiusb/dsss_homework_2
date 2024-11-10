import unittest
from math_quiz import random_int, random_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        for _ in range(1000): # Test a large number of random operators
            rand_op = random_operator()
            self.assertTrue(rand_op in ['+', '-', '*'])

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '-', '6 - 3', 3),
                (9, 8, '*', '9 * 8', 72)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate(num1, num2, operator)
                self.assertEquals(expected_problem, problem)
                self.assertEquals(expected_answer, answer)

if __name__ == "__main__":
    unittest.main()
