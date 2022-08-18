import time
from page_object import Selectors


def test_page(browser, username, password):
    browser.get(browser.url)
    a = browser.find_element(*Selectors.BUTTON_MY_ACCOUNT)
    time.sleep(2)
    a.click()
    time.sleep(2)
    browser.find_element(*Selectors.BUTTON_LOGIN).click()
    time.sleep(2)
    browser.find_element(*Selectors.USERNAME).send_keys(username)
    browser.find_element(*Selectors.PASSWORD).send_keys(password)
    time.sleep(2)
    browser.find_element(*Selectors.LOGIN).click()
    time.sleep(2)
