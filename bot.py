import os
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class AmazonBot():

    def __init__(self,user_agent):
        options=webdriver.ChromeOptions()
        self.options = options

        
        options.add_argument("--user-data-dir="+os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data"))         
        options.add_argument("--profile-directory=Default")    
        
        self.user_agent = user_agent

        options.add_argument("user-agent="+user_agent)    
   
    
        driver  = uc.Chrome(options=options)
        self.driver = driver
    

    def go_to_product(self,link):
        driver = self.driver

        driver.get(link)


    def put_to_shopping_card(self):
        driver = self.driver
    
 
        shopping_cart_button = driver.find_element(By.XPATH, '//*[@id="submit.add-to-cart"]//*')
        shopping_cart_button.click()

    
        try:
            insurance_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')))
            insurance_button.click()
            
            go_to_checkout_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="attach-sidesheet-checkout-button"]/span/input')))
            go_to_checkout_button.click()
            
            return

        except:pass
     
        go_to_checkout_button2 = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input'))) 
        go_to_checkout_button2.click()


    def buy_now(self):
        driver = self.driver

        buy_now_button = driver.find_element(By.XPATH,'//*[@id="placeYourOrder"]/span/input')
        buy_now_button.click()
        
        time.wait(100)











        











        






