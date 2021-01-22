from html.parser import HTMLParser
import requests


class LinkParser(HTMLParser):
    """This is a link parser that inherits the HTMLParser class
    usefull for the feed method
    this class will get a single web page and then return a lin

    """

    def __init__(self):
        super().__init__()
        self.link_array = []

    def handle_starttag(self, tag, attrs):
        """
        These methods should not be called externally,
        these are being extened from the HTMLParser class
        """
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.link_array.append(attr)

    def get_sub_links(self):
        # we only need to add them to the
        return set(self.link_array)


def get_sub_links(url, verbose):
    """This is a helper function. We should only need to
    export this function outside.
    """
    link_parser = LinkParser()
    response = requests.get(url)
    if verbose:
        print(f"Visited {url} with status code {response.status_code}")
    if response.status_code == 200:
        link_parser.feed(response.text)
        return [i[1] for i in link_parser.get_sub_links()]

    # handles for the cases where there is an error with the request
    return []
