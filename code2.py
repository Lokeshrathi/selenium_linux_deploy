from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
firefoxOptions = Options()
keys_ = ['acrylic paint tubes','acrylic colors']
order = []
product_link = []
grocery = []
product_list = []
product_price = []
product_review = []
product_rating = []
volume = []
keyword = []
firefoxOptions.add_argument("-headless")
driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver", options=firefoxOptions)
for i in keys_:
    url_ = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".format(i)
    print(i)
    driver.get(url_)
    time.sleep(5)
    product_list_ = driver.find_elements_by_xpath('//*[@class = "s1Q9rs"]')
    for x in product_list_:
        x=x.text
        product_list.append(x)
    
    product_price_ = driver.find_elements_by_xpath('//*[@class = "_30jeq3"]')
    for x1 in product_price_:
        x1=x1.text
        product_price.append(x1)

print(product_list)
print(product_price)
driver.quit()
