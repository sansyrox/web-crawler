import unittest
from link_parser import get_sub_links
from web_crawler import WebCrawler
import requests
import sys


class TestWebCrawler(unittest.TestCase):
    """Create a testing class object that tests all the web crawler methods"""

    def test_crawler(self):
        web_crawler = WebCrawler(
            url="http://localhost:5000", max_threads=32, max_pages=float("inf")
        )

        self.assertEqual(
            sorted(list(web_crawler.crawl())),
            sorted(
                [
                    "http://localhost:5000/com",
                    "http://localhost:5000/test",
                    "http://localhost:5000/test123",
                ]
            ),
        )

        self.assertNotEqual(
            sorted(list(web_crawler.crawl())),
            sorted(
                ["https://google.com", "http://localhost:5000/com", "/test", "/test123"]
            ),
        )

    def test_get_sub_links(self):
        sub_links = get_sub_links("http://localhost:5000")
        self.assertEqual(
            sorted(list(sub_links)),
            sorted(
                ["https://google.com", "http://localhost:5000/com", "/test", "/test123"]
            ),
        )
        self.assertNotEqual(sorted(list(sub_links)), [])

    def test_get_host(self):
        web_crawler = WebCrawler.get_host("http://localhost:5000")
        self.assertEqual(web_crawler, "localhost:5000")


if __name__ == "__main__":

    if requests.get("http://localhost:5000").status_code != 200:
        sys.exit("Please run the test server")

    unittest.main()
