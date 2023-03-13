import unittest
from substring import get_max_substring


class TestSubstrings(unittest.TestCase):
    def test_substring_case_1(self):
        sample_string = "abcabcbb"
        result = get_max_substring(sample_string)
        self.assertEqual(result, 3)

    def test_substring_case_2(self):
        sample_string = "bbbbb"
        result = get_max_substring(sample_string)
        self.assertEqual(result, 1)

    def test_substring_case_3(self):
        sample_string = "pwwkew"
        result = get_max_substring(sample_string)
        self.assertEqual(result, 3)

    def test_substring_case_4(self):
        sample_string = "12p wkew"
        result = get_max_substring(sample_string)
        self.assertEqual(result, 7)

    def test_substring_case_5(self):
        sample_string = "12p wke@#w"
        result = get_max_substring(sample_string)
        self.assertEqual(result, 9)

    def test_substring_case_6(self):
        sample_string = "".join("s" for _ in range(50000))
        result = get_max_substring(sample_string)
        self.assertEqual(result, 1)

    def test_substring_case_exceed_max_length(self):
        sample_string = "".join("s" for _ in range(50001))
        with self.assertRaises(ValueError):
            get_max_substring(sample_string)

    def test_substring_case_empty_string(self):
        sample_string = ""
        with self.assertRaises(ValueError):
            get_max_substring(sample_string)


if __name__ == "__main__":
    unittest.main()
