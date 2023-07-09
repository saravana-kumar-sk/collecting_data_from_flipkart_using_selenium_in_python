from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from dotenv import load_dotenv
import os
import pandas as pd
def startpy():
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    search=driver.find_element("xpath",'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    search.click()
    search.send_keys("Mobiles")
    search.send_keys(Keys.RETURN)
    count=2

    for i in range(2,6):
        time.sleep(3)   
        mob_title=driver.find_elements("xpath","//*[@class='_4rR01T']")
        print(len(mob_title))
        for title in mob_title:
            ti=title.text
            mobile_titles.append(ti)
        mob_amount=driver.find_elements("xpath","//*[@class='_30jeq3 _1_WHN1']")
        for amount in mob_amount:
            amt=amount.text
            mobile_amount.append(amt)
        mob_description=driver.find_elements("xpath","//*[@class='_1xgFaf']")
        for description in mob_description:
            des=description.text
            mobile_description.append(des)
        #driver.find_element("xpath",f"//*[@class='ge-49M'][{i}]".click())
    mobile_details['Title']=mobile_titles
    mobile_details['Amount']=mobile_amount
    mobile_details['description']=mobile_description

    details=pd.DataFrame(mobile_details)
    details.to_csv('data.csv')
    print(details)
    print(details.head(10))
load_dotenv()
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
mobile_titles=[]
mobile_amount=[]
mobile_description=[]
mobile_details={}


if __name__=='__main__':
    startpy()
