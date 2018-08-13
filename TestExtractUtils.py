import unittest

from conf import creds
from utils import extract_utils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_login(self):

        pass


if __name__ == '__main__':
    unittest.main()
