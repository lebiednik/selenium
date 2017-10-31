
from selenium import webdriver


#profile = webdriver.FirefoxProfile()
#profile.native_events_enabled = False
driver = webdriver.PhantomJS()
driver.get('http://www.cnn.com/')
driver.quit()


