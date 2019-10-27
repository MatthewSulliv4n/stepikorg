from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    NAME_PRODUCT_ALERT_MSG = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_PRODUCT_ALERT_MSG = (By.CSS_SELECTOR, ".alertinner > p strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
