import sys
from selenium import webdriver

if len(sys.argv) > 1 and sys.argv[1] == 'chrome':
    browser = webdriver.Chrome("/home/robson/work/software/utils/selenium/geckodriver")
else:
    browser = webdriver.Firefox(executable_path="/opt/firefox/plugins/geckodriver")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
