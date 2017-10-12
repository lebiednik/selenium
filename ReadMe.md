Install 
sudo pip install selenium
sudo pip install -e git://github.com/davedash/Alexa-Top-Sites.git#egg=alexa-top-sites

download newest gecko driver
https://github.com/mozilla/geckodriver/releases

from download location
tar xvzf geckodriver-vX.X.0-linux64.tar.gz
sudo cp geckodriver ../../../etc/python/

from project location
export PATH=$PATH:/etc/python
