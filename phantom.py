from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import datetime
import urllib2
import os
import signal
import random


#number of top sites to get max 50 without license
TOP_N = 50 
# Top sites in which country or 'global'
COUNTRY_CODE = 'US'
top_sites = []
BASE_URL="http://www.alexa.com/topsites"

#This landing page has entries 1 - 50
if COUNTRY_CODE != "global":

    response = urllib2.urlopen(BASE_URL + "/countries/" + COUNTRY_CODE)
else:
    response = urllib2.urlopen(BASE_URL)
html = response.read()

# scrape the combined HTML for domain names
tokens = html.split("<")
for token in tokens:
    if token.startswith("a href=\"/siteinfo/"):
        subtokens = token.split("\">")[0].split("/")
        site = subtokens[2]
        if len(top_sites) < TOP_N:
            top_sites.append(site)
#print top_sites

base = 'http://www.'
while True:
    site = random.choice(top_sites)
    print site
    driver = webdriver.PhantomJS()
    driver.get(base+site)
    driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()
"""
for url in top_sites:
    print url
    driver = webdriver.PhantomJS()
    driver.get(base+url)
    driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()
"""


