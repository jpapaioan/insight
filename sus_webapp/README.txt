Here is everything for the webapp, locally hosted for debugging purposes but identical code in an AWS server hosted on a site with the domain, www.standup-sommelier.com

run.py creates the flask instance, found in __init__.py that points to routes.py

routes.py contains the code actually reads in the data, creates the submission form for user input on the site, filters the comedian list according to input, and initializes variables as input for html templates to display the results

com_methods.py contains all functions that are used in routes.py for extracting comedians and URL's for hyperlinking

templates dir contains the html templates for the main page and results page

static contains the background images for the site, the main dataset of comedians and classifications, and the css/js files needed for site customization
