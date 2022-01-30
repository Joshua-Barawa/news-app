import unittest
from news_article import Article


class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_article = Article("dff", "dff", "dff", "dff", "dff", "dff", "dff")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))
