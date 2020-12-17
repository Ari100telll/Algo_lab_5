import unittest
from KnuthMorrisPratt import prefix_function


class TestKnuthMorrisPratt(unittest.TestCase):
    def test_strings(self):
        self.assertEqual(2, prefix_function("abaabaaaabaabaaab", "aabaa"))
        self.assertEqual(4, prefix_function("abaabaaaabaabaaab", "baaaab"))
        self.assertEqual(12, prefix_function("abaabaaaabaabaaab", "baaab"))

    def test_no_substring(self):
        self.assertEqual(-1, prefix_function("abaabaaaabaabaaab", "ccac"))
        self.assertEqual(-1, prefix_function("abaabaaaabaabaaab", "bb"))
        self.assertEqual(-1, prefix_function("abaabaaaabaabaaab", "aabab"))

    def test_equal_strings(self):
        self.assertEqual(0, prefix_function("abaabaaaabaabaaab", "abaabaaaabaabaaab"))
        self.assertEqual(0, prefix_function("ccc", "ccc"))
        self.assertEqual(0, prefix_function("adasdasda", "adasdasda"))

    def test_substring_longer(self):
        self.assertEqual(-1, prefix_function("abaabaaaabaabaaab", "abaabaaaabaabaaaba"))


if __name__ == '__main__':
    unittest.main()
