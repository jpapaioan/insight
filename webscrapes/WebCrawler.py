#!/usr/bin/env python
import logging
import csv
from selenium import webdriver
from urllib.parse import urldefrag, urljoin
from collections import deque
from bs4 import BeautifulSoup
from string import ascii_uppercase
import os




class SeleniumCrawler(object):

    def __init__(self, base_url, exclusion_list, inclusion_list, output_file='example.csv', start_url=None):

        assert isinstance(exclusion_list, list), 'Exclusion list - needs to be a list'
        assert isinstance(inclusion_list, list), 'Inclusion list - needs to be a list'

        
        dir = os.getcwd()           #get driver

        chrome_driver_path = dir + '/chromedriver'
        self.browser = webdriver.Chrome(chrome_driver_path)

        self.base = base_url

        self.start = start_url if start_url else base_url  #If no start URL is passed use the base_url

        self.exclusions = exclusion_list  #List of URL patterns we want to exclude

        self.inclusions = inclusion_list #List of URL patterns we want to include
        
        self.crawled_urls = []  #List to keep track of URLs we have already visited

        self.url_queue = deque([self.start])  #Add the start URL to our list of URLs to crawl

        self.output_file = output_file


    def get_page(self, url):
        try:
            self.browser.get(url)
            return self.browser.page_source
        except Exception as e:
            logging.exception(e)
            return

    def get_soup(self, html):
        if html is not None:
            soup = BeautifulSoup(html, 'lxml')
            return soup
        else:
            return

    def get_links(self, soup):

        for link in soup.find_all('a', href=True):
            link = link['href']
            if any(e in link for e in self.exclusions):
                continue
            url = urljoin(self.base, urldefrag(link)[0])
            if url not in self.url_queue and url not in self.crawled_urls:
                if url.startswith(self.base):
                    self.url_queue.append(url)

    def get_data(self, soup):

        try:
            result = soup.find("div", {"class":"comedian-desc"}).text  #trying to extract comedian bios
        except:
            result = None
        return result

    def csv_output(self, url, title):

        with open(self.output_file, 'a', encoding='utf-8') as outputfile:

            writer = csv.writer(outputfile)
            writer.writerow([url, title])

    def run_crawler(self):
        while len(self.url_queue): #If we have URLs to crawl - we crawl
            current_url = self.url_queue.popleft() #We grab a URL from the left of the list
            self.crawled_urls.append(current_url) #We then add this URL to our crawled list
            html = self.get_page(current_url)
            if self.browser.current_url != current_url: #If the end URL is different from requested URL - add URL to crawled list
                self.crawled_urls.append(current_url)
            soup = self.get_soup(html)
            if soup is not None:  #If we have soup - parse and write to our csv file
                self.get_links(soup)
                print('curr_url: ', current_url)
                title = self.get_data(soup)
                self.csv_output(current_url, title)


if __name__ == '__main__':
    base_url = 'https://www.comedyworks.com/comedians/'
    start_url = 'https://www.comedyworks.com/comedians?page='

    for i in range(1,51):
        curr_url = start_url + str(i)
        a = SeleniumCrawler(base_url, ['?'], [''], start_url = curr_url)
        a.run_crawler()



