import time 

def test_guest_should_see_add_to_basket_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
        isElementPresent = True
    except:
        isElementPresent = False
    time.sleep(5)
    assert isElementPresent, {'Элемент не найден.'}
        