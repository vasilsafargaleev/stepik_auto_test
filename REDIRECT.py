from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input.send_keys(y)

    button3 = browser.find_element(By.XPATH, '//button[text()="Submit"]' )
    button3.click()
finally:
    time.sleep(5)
    browser.quit()
