from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("treasure")
    value = x.get_attribute("valuex")
    value = str(math.log(abs(12*math.sin(int(value)))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(value)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
