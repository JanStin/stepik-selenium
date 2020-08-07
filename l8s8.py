from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("firstname")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("lastname")

    email = browser.find_element_by_name("email")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
