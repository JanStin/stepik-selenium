from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12*math.sin(int(x)))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(x)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


