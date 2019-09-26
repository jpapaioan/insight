#!/usr/bin/env python

# web crawling comedy works' comedians pages for bio texts

from WebCrawler import *

base_url = 'https://www.comedyworks.com/comedians/'
start_url = 'https://www.comedyworks.com/comedians?page='

for i in range(1,51):
        curr_url = start_url + str(i)
        a = SeleniumCrawler(base_url, ['?'], [''], start_url = curr_url)
        a.run_crawler()

