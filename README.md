# WebCrawler

The approach followed here is a distributed breadth first search across a pool of threads.

## Usage

```
pipenv shell 
pipenv install

usage: python main.py [--url="https://monzo.com"] [--max-pages="5"] [--max_threads=5]


optional arguments:
  -h, --help            show this help message and exit
  --max_pages           The maximum number of pages it needs to 
                        crawl. All the other pages are ignored.

  --url                 The url required. This defaults to monzo.com

  --max_threads         This is the number of threads that we can allot. See the codebase for the default algo used
```


## Logging

If the verbose mode is set to true, the visited websites are logged to stdout.

## Testing

A dummy flask server is set up before running the tests. One of the test queries the local server to check for the correctness of the web crawler.
