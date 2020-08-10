import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    WebDriverWait(browser, 15).until_not(EC.invisibility_of_element((By.CSS_SELECTOR , ".string-quiz__textarea")))

    answer = math.log(int(time.time()))
    text_field = browser.find_element_by_css_selector('.string-quiz__textarea')
    text_field.send_keys(str(answer))

    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    WebDriverWait(browser, 15).until_not(EC.invisibility_of_element((By.CSS_SELECTOR , ".smart-hints__hint")))
    feedback = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert feedback == 'Correct!', f'Value Correct! != {feedback}'
