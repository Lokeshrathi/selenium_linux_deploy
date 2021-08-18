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
        keyword.append(i)
    
    product_price_ = driver.find_elements_by_xpath('//*[@class = "_30jeq3"]')
    for x1 in product_price_:
        x1=x1.text
        product_price.append(x1)
        
    volume_ =  browser.find_elements_by_xpath('//*[@class="_3Djpdu"]')
    for x5 in volume_:
        x5=x5.text
        volume.append(x5)
     
    product_rate_ = browser.find_elements_by_xpath('//*[@class = "_2_R_DZ"]')
    for x3 in product_rate_:
        x3=x3.text
        product_rating.append(x3)
    
    product_review_ = browser.find_elements_by_xpath('//*[@class = "_1lRcqv"]')
    for x2 in product_review_:
        x2=x2.text
        product_review.append(x2)
        
req = pd.DataFrame(list(zip(product_list, product_price,keyword,product_review,product_rating,volume,product_link)),
                   columns = ['Name', 'Price','Keyword','product_review','product_rating','volume','Product_link'])
req['check']= 1
fill = req.groupby(['Keyword']).agg({'check':'cumsum'})
fill.rename({'check':'Order'},axis=1,inplace=True)
final = pd.concat([req,fill],axis=1)
final.drop({'check'},axis=1,inplace=True)
final.head()
driver.quit()
