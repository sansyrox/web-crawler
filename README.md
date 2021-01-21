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
