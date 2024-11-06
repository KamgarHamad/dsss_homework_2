import unittest
from math_quiz import generate_random_number, choose_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # Test that choose_operator only returns valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Run multiple times due to randomness
            operator = choose_operator()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):
        # Test specific cases for create_math_problem to verify correct problem string and answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 3, '-', '5 - 3', 2),
            (5, 4, '*', '5 * 4', 20),
            (10, 2, '+', '10 + 2', 12),
            (9, 2, '-', '9 - 2', 7),
            (8, 3, '*', '8 * 3', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
