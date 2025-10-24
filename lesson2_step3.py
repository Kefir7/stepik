from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = int(browser.find_element(By.ID, "num1").text)
    y_element = int(browser.find_element(By.ID, "num2").text)
    result = x_element + y_element
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()