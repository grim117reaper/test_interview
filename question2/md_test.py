from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests
from bs4 import BeautifulSoup


category = ["cpu cooler","gaming headset","mouse","ram"]
name = []
price = []
source = []
categories=[]
print("sample test case started")
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.add_argument("--headless")
headers = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})


for x in category:
    driver = webdriver.Firefox(options=fireFoxOptions)  
    driver.get("https://mdcomputers.in/")  
    #identify the Google search text box and enter the value  
    driver.find_element(By.CSS_SELECTOR,".autosearch-input").send_keys(x,Keys.RETURN)
    time.sleep(4)
    items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[contains(@class, "products-category")]')))
    url = driver.current_url
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, features="lxml")
    # for price
    my_div= soup.find("div",{"class" : "products-category"})
    sub_elements = my_div.findAll("div" ,{"class" : "product-item-container"})

    for y in sub_elements:
        name_value = y.find("div" ,{"class" : "right-block right-b"}).find("a").get_text()
        name.append(name_value.strip())
        price_span = y.find("span",{"class" : "price-new"})
        price.append(float(price_span.get_text()[1:].replace(",","")))
        source.append("mdcomputers")
        categories.append(x)
        # print("{} : {}".format(name,str(price)))
    driver.close()
df = pd.DataFrame(list(zip(name, price, categories,source)),columns =['Name', 'price',"category","source"])
df.to_csv("raw_data_md.csv")