#option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
#option1.click()


from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link="http://suninjuly.github.io/get_attribute.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")

    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    button2.click()
    button3 = browser.find_element(By.XPATH, '//button[text()="Submit"]' )
    button3.click()

finally:
    time.sleep(5)
    browser.quit()
