import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("petrov@gmail.com")
    file_input = browser.find_element(By.ID, "file") # поле для загрузки файла
    file_input.send_keys(file_path) # загрузка
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    time.sleep(10)
        # закрываем браузер после всех манипуляций
    browser.quit()