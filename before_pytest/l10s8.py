from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной   
    wait = WebDriverWait(browser, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12*math.sin(int(x)))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(x)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    