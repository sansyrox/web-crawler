import queue
from threading import Lock
import link_parser
from concurrent.futures import ThreadPoolExecutor


class WebCrawler:
    """
    This is a web crawler class that takes in the default values of
    url, threads and max pages that it can parse

    This will create a thread based system to handle blocking requests
    and scrape the web

    """

    def __init__(self, url, max_threads, max_pages) -> None:
        """
        :type url: str
        :type max_threads: int
        :type max_pages: int or float("inf")
        :rtype: None
        """
        self.initial_url = url
        self.threads = max_threads
        self.max_pages_to_visit = max_pages
        self.visited_lock = Lock()
        self.web_page_visited = set()
        self.web_pages_to_visit = queue.Queue()
        self.web_pages_to_visit.put(url)  # decide if put or put no wait

    @classmethod
    def get_host(cls, url):
        """
        :type url: str
        :rtype: str
        """
        return url.split("//")[1].split("/")[0]

    def crawler(self):
        """
        :rtype: None
        """
        while True:
            url = None
            try:
                # we create a non blocking thread as we don't want the threads
                # to wait and the program should exit when the queue is empty
                url = self.web_pages_to_visit.get(block=False)
            except queue.Empty:
                return

            sub_urls = link_parser.get_sub_links(url)

            for sub_url in sub_urls:
                with self.visited_lock:
                    if sub_url[0] == "/":
                        # This will handle the case where the website is only linking to subdomains
                        # e.g. /blog
                        new_url = f"{url.strip('/')}/{sub_url.strip('/')}"
                        if (
                            new_url not in self.web_page_visited
                            and len(self.web_page_visited) < self.max_pages_to_visit
                        ):
                            self.web_pages_to_visit.put(new_url)
                            self.web_page_visited.add(new_url)

                    elif (
                        self.get_host(sub_url) == self.get_host(self.initial_url)
                        and sub_url not in self.web_page_visited
                        and len(self.web_page_visited) < self.max_pages_to_visit
                    ):
                        self.web_pages_to_visit.put(sub_url)
                        self.web_page_visited.add(sub_url)

    def crawl(self):
        """
        :rtype: set
        """

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for _ in range(self.threads):
                executor.submit(self.crawler)

        return set(self.web_page_visited)
