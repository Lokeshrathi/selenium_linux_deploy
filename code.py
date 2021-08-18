from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path =CHROMEDRIVER_PATH, options=chrome_options)
driver.get("https://www.flipkart.com/search?q=acrylic%20colors&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off%22")
print(driver)

list_= driver.find_elements_by_xpath('//*[@class = "s1Q9rs"]')
print("Here I have entered")
print(list_)
names = []
for x in list_:
     names.append(x)
print(names)
driver.close()
