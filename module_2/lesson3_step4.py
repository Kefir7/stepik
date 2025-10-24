import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # time.sleep(10)
    #     # закрываем браузер после всех манипуляций
    # browser.quit()
    print(browser.switch_to.alert.text)