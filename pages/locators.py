from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    NAME_PRODUCT_ALERT_MSG = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_PRODUCT_ALERT_MSG = (By.CSS_SELECTOR, ".alertinner > p strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")
