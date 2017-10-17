Install \n
sudo pip install selenium bs4 \n

download newest gecko driver \n
https://github.com/mozilla/geckodriver/releases \n

from download location
tar xvzf geckodriver-vX.X.0-linux64.tar.gz
sudo cp geckodriver ../../../etc/python/

from project location
export PATH=$PATH:/etc/python

For alexa_static_scraper.py
sudo pip install -e git://github.com/davedash/Alexa-Top-Sites.git#egg=alexa-top-sites

scraper.py
retrieves the top 50 sites from https://www.alexa.com/topsites/countries/US
Only the top 50 are available for free.
Uses the selenium wrapper to launch Firefox or Chrome browsers that render the site and then close

alexa_static_scraper.py
retrieves the top 1M sites (globally) from a csv for ingest
Uses the selenium wrapper to launch Firefox or Chrome browsers that render the site and then close
