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
    driver.get("https://www.amazon.in/")  
    #identify the Google search text box and enter the value  
    driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys(x,Keys.RETURN)
    time.sleep(4)
    items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[contains(@class, "sg-col-inner")]')))
    url = driver.current_url
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, features="lxml")
    # for price
    my_div= soup.find("div",{"class" : "s-desktop-width-max s-desktop-content s-wide-grid-style-t1 s-opposite-dir s-wide-grid-style sg-row"})
    sub_elements = my_div.findAll("div" ,{"class" : "a-section a-spacing-small a-spacing-top-small"})

    for y in sub_elements:
        name.append(y.find("span" ,{"class" : "a-size-medium a-color-base a-text-normal"}).get_text().strip())
        price_span = y.find("span",{"class" : "a-offscreen"})
        price.append(float(price_span.get_text()[1:].replace(",","")))
        source.append("amazon")
        categories.append(x)
        # print("{} : {}".format(name,str(price)))
    driver.close()
df = pd.DataFrame(list(zip(name, price, categories, source)),columns =['Name', 'price',"category","source"])
df.to_csv("raw_data_amazon.csv")
