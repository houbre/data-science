import unittest
import newsapi
from tests.newsapi.functions import check_dates


class CheckNoKeywords(unittest.TestCase):

    def test_empty_list_error(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', [])

    def test_empty_string_keyword(self):
         with self.assertRaises(Exception):
            newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', '')

    def test_no_keywords_arguments(self):
        with self.assertRaises(Exception):
            newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9')


class test_lookback_days(unittest.TestCase):
    
    def test_correct_dates(self):
        self.assertTrue(check_dates(newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', ['apple', 'google'])))

    def test_more_than_ten(self):
        self.assertFalse(check_dates(newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', ['apple', 'google'], 15)))

    

class CheckKeywordsLetters(unittest.TestCase):

    def test_single_keyword(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', 'hello123bye')

    def test_multiple_keyword(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news('5567996d16e74b9b9c3e5e5091be66b9', ['hellobye', 'joe', 'boehm', 'haha123haha'])


if __name__ == '__main__':
    unittest.main()