import unittest
from password_analyzer import calculate_entropy, basic_checks

class TestPasswordAnalyzer(unittest.TestCase):

    def test_entropy_increases_with_complexity(self):
        self.assertLess(
            calculate_entropy("abcd"),
            calculate_entropy("abcd1234")
        )
        self.assertGreater(
            calculate_entropy("All2@6b#3!"),
            25
        )

    def test_basic_checks_pass(self):
        result = basic_checks("Password123!")
        self.assertTrue(result["length"])
        self.assertTrue(result["uppercase"])
        self.assertTrue(result["lowercase"])
        self.assertTrue(result["digit"])
        self.assertTrue(result["special"])

    def test_basic_checks_fail(self):
        result = basic_checks("weak")
        self.assertFalse(result["length"])
        self.assertFalse(result["uppercase"])
        self.assertTrue(result["lowercase"])  # 'weak' is lowercase
        self.assertFalse(result["digit"])
        self.assertFalse(result["special"])

if __name__ == "__main__":
    unittest.main()

