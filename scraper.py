from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import urllib2
import os

#number of top sites to get max 50 without license
TOP_N = 10
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
print top_sites

base = 'http://www.'
"""
#Open the sites using Firefox
for url in top_sites:
    driver = webdriver.Firefox()
    driver.get(base+url)
    driver.close()
"""
#Open the sites using Chrome
chromedriver = '/etc/python/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver

for url in top_sites:
    driver = webdriver.Chrome(chromedriver)
    driver.get(base+url)
    driver.quit()
