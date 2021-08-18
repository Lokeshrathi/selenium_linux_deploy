from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import numpy as np
browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()
