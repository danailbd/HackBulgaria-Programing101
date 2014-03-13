import unittest
import string_utils

class StrungUtilsTests(unittest.TestCase):

    def test_lines(self):
        self.assertEqual(["aaa", "bbb", "ccc"], string_utils.lines("aaa\nbbb\nccc"))

    def test_unlines(self):
        self.assertEqual("aa\nvv\n\dsf\nder", string_utils.unlines(["aa", "vv", "\dsf", "der"]))

    def test_words(self):
        self.assertEqual(["aa", "vv", "\dsf", "der"], string_utils.words("aa vv \dsf der"))

    def test_unwords(self):
        self.assertEqual("aa vv \dsf der", string_utils.unwords(["aa", "vv", "\dsf", "der"]))

    def test_tab_to_spaces(self):
        self.assertEqual("as    sdfas    dfa", string_utils.tabs_to_spaces("as\tsdfas\tdfa"))

if __name__ == '__main__':
    unittest.main()
