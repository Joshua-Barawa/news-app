import unittest
from news_source import Source


class TestSource(unittest.TestCase):

    def setUp(self):
        self.new_source = Source("abc", "ABC-News")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


