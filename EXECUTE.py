from tkinter import Y
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math 

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    button2.click()
    button3 = browser.find_element(By.XPATH, '//button[text()="Submit"]' )
    button3.click()
finally:
    time.sleep(5)
    browser.quit()
