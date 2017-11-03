# Install
    sudo pip install selenium

## download newest gecko driver
    https://github.com/mozilla/geckodriver/releases
    from download location
    tar xvzf geckodriver-vX.X.0-linux64.tar.gz
    sudo cp geckodriver /etc/python/
## download the newest chromedriver
    https://chromedriver.storage.googleapis.com/index.html?path=2.33/
    from download location
    unzip chromedriver chromedriver_linux64.zip
    sudo cp chromedriver /etc/python
## install chrome
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
    sudo apt-get update
    sudo apt-get install google-chrome-stable
## install phantomjs raspberry pi
    cd /tmp
    wget https://github.com/aeberhardo/phantomjs-linux-armv6l/archive/master.zip
    unzip master.zip
    cd phantomjs-linux-armv6l-master
    bunzip2 *.bz2 && tar xf *.tar
    sudo cp phantomjs-1.9.0-linux-armv6l/bin/phantomjs /usr/bin

## from project location
    export PATH=$PATH:/etc/python

## For alexa_static_scraper.py
    sudo pip install -e git://github.com/davedash/Alexa-Top-Sites.git#egg=alexa-top-sites

# scraper.py
    retrieves the top 50 sites from https://www.alexa.com/topsites/countries/US
    Only the top 50 are available for free.
    Uses the selenium wrapper to launch Firefox or Chrome browsers that render the site and then close

# alexa_static_scraper.py
    retrieves the top 1M sites (globally) from a csv for ingest
    Uses the selenium wrapper to launch Firefox or Chrome browsers that render the site and then close
