import argparse
from web_crawler import WebCrawler
from pprint import pprint
import os


def initialise_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url", help="enter the url in the form of http[s]://[*.]abc.com"
    )
    parser.add_argument(
        "--max_threads",
        help="enter the maximum number of pages that need to be crawled",
    )
    parser.add_argument(
        "--max_pages", help="limit the maximum pages that the crawler can parse"
    )
    parser.add_argument(
        "-v", "--verbose", help="increase the verbose output", type=bool, default=False
    )

    args = parser.parse_args()

    return {
        "url": args.url if args.url else "https://www.scrapehero.com/",
        "max_threads": args.max_threads
        if args.max_threads
        else min(32, os.cpu_count() + 4),  # is the max workers default value in python
        "max_pages": args.max_pages if args.max_pages else float("inf"),
        "verbosity": args.verbose,
    }


if __name__ == "__main__":
    args = initialise_arguments()
    web_crawler = WebCrawler(**args)
    pprint(web_crawler.crawl())
