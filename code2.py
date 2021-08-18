from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
firefoxOptions = Options()
firefoxOptions.add_argument("-headless")
driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver", options=firefoxOptions)
driver.get("https://www.flipkart.com/search?q=acrylic%20colors&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off%22")
time.sleep(5)
list_= driver.find_element_by_xpath('//*[@class = "s1Q9rs"]').text
print("Here I have come",list_)
driver.quit()
