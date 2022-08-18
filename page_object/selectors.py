from selenium.webdriver.common.by import By


class Selectors:
    BUTTON_MY_ACCOUNT = (By.CSS_SELECTOR, "li.dropdown")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "a[href*='account/login']")
    USERNAME = (By.CSS_SELECTOR, "input[name = 'email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN = (By.CSS_SELECTOR, "input[value='Login']")
