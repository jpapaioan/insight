#!/usr/bin/env python

from WebCrawler import *

start_url = 'https://scrapsfromtheloft.com/tag/stand-up-transcripts/'
base_url = 'https://scrapsfromtheloft.com'

a = SeleniumCrawler(base_url, ['?'], [''], start_url)
a.run_crawler()
