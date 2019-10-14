This directory contains webscraping/webcrawling code in python using Selenium, BeautifulSoup and a ChromeDriver for automated programmatically controlled browsing.

comedy_works.py webscrapes all comedian profiles from www.comedyworks.com which was a first source of meta-data(descriptions of comedians, not actual content)

full_transcripts.ipynb webscrapes full comedy transcripts from www.scrapsfromtheloft.com

transcripts_EDA_cleanup.ipynb trims down the initially gathered data removing miscellaneous/unwanted transcripts that weren't of comedy specials and cleans up the URL's to extract comedian names, culminating in a dataframe of comedians with the full collection of their transcript(s)
