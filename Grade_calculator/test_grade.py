import unittest
from unittest.mock import patch
from io import StringIO
from grade import calculate_grade, student_grade_calculator

class TestStudentGradeCalculator(unittest.TestCase):

    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), 'A')
        self.assertEqual(calculate_grade(85), 'B')
        self.assertEqual(calculate_grade(75), 'C')
        self.assertEqual(calculate_grade(65), 'D')
        self.assertEqual(calculate_grade(55), 'F')
        self.assertEqual(calculate_grade(-5), 'Invalid Score')
        self.assertEqual(calculate_grade(105), 'Invalid Score')

    def test_student_grade_calculator_valid_input(self):
        input_values = ['3', 'Math', '90', 'Science', '85', 'English', '95']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                student_grade_calculator()
                output = mock_stdout.getvalue().strip()

        self.assertIn("Total Score: 270", output)
        self.assertIn("Average Score: 90.00", output)
        self.assertIn("Overall Grade: A", output)

    def test_student_grade_calculator_invalid_input(self):
        input_values = ['4', 'History', '75', 'Geography', '88', 'Music', '105', 'Math', 'abc']
        with patch('builtins.input', side_effect=input_values):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                student_grade_calculator()
                output = mock_stdout.getvalue().strip()

        self.assertIn("Invalid score. Score should be between 0 and 100.", output)
        self.assertNotIn("Total Score:", output)

if __name__ == '__main__':
    unittest.main()
