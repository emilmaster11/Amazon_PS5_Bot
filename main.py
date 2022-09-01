from re import A
import time 
import multiprocessing
from cgitb import enable
from tkinter.tix import Select
from selenium import webdriver
import undetected_chromedriver as uc
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException



def PS5_bot():

 options=webdriver.ChromeOptions()

 options.add_argument("--start-maximized")
 options.add_argument("--user-data-dir=C:\\Users\\emilb\\Desktop\\Python_projekte\\BOTS\\Chrome_Profile\\GoogleChromeProfile2");
 options.add_argument("--profile-directory=Profile2");

 chrome_browser=uc.Chrome(executable_path=r'C:\Users\emilb\Desktop\Python_projekte\BOTS\driver\chromedriver.exe',options=options)


 try:
     chrome_browser.get("https://www.amazon.de/PlayStation-Horizon-Forbidden-West-Voucher/dp/B0B1MPZWJG/ref=sr_1_2?keywords=ps5+horizon+bundle&sprefix=ps5+horzon+bu%2Caps%2C141&sr=8-2");

    
 except:
    time.sleep(100)


 while True:
    try:
     waren_korb_finden = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(By.CSS_SELECTOR, value = "#add-to-cart-button"))
     break 
    
    except:
     chrome_browser.get("https://www.amazon.de/PlayStation-Horizon-Forbidden-West-Voucher/dp/B0B1MPZWJG/ref=sr_1_2?keywords=ps5+horizon+bundle&sprefix=ps5+horzon+bu%2Caps%2C141&sr=8-2");
    
 while True:
    try:
     waren_korb_finden.click()
     break
    except:
        chrome_browser.get("https://www.amazon.de/PlayStation-Horizon-Forbidden-West-Voucher/dp/B0B1MPZWJG/ref=sr_1_2?keywords=ps5+horizon+bundle&sprefix=ps5+horzon+bu%2Caps%2C141&sr=8-2");


 while True:
    try:
        jetzt_kaufen = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(By.CSS_SELECTOR, value = "#submitOrderButtonId > span > input")).click()
        break

    except:
       chrome_browser.refresh()
   
 

 time.sleep(100)

if __name__ == '__main__':
    PS5_bot()