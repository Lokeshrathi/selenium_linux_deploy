from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
firefoxOptions = Options()
firefoxOptions.add_argument("-headless")
browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver", options=firefoxOptions)
browser.get('https://www.linuxhint.com')
time.sleep(5)
print('Title: %s' % browser.title)
browser.quit()
