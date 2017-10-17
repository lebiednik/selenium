from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import alexa

top = alexa.top_list(10)
base = 'http://www.'
for url in top:
    driver = webdriver.Firefox()
    driver.get(base+url[1])
    driver.close()
