import unittest
from subprocess import call
import os

class SpacifyTest(unittest.TestCase):
    """SpacifyTest"""
    def setUp(self):
        self.TEST_STRING = "fdsfasdf\t\tdfa dfs\t\\dasgsdt"
        self.file_name = "testFile"
        self.file_handler = open(self.file_name, 'w')
        self.file_handler.write(self.TEST_STRING)
        self.file_handler.close()

    def test_spacify(self):
        call("python3 spacify.py " + self.file_name, shell=True)
        file = open(self.file_name)
        content = file.read()
        self.assertRaises(ValueError, content.index, '\t')
        file.close()

    def setDown(self):
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()
