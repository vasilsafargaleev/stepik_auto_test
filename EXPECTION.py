from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    WebDriverWait(browser,12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input.send_keys(y)

    button3 = browser.find_element(By.ID, "solve" )
    button3.click()
finally:
    time.sleep(10)
    browser.quit()



