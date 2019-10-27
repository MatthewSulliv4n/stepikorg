from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product(self):
        add_product_btn = self.browser.find_element(
            *ProductPageLocators.ADD_PRODUCT_BTN)
        add_product_btn.click()

    def assert_text_in_alert(self, path_to_text, path_in_alert):
        text = self.browser.find_element(
            *path_to_text).text
        path_in_alert = self.browser.find_element(
            *path_in_alert)
        text_in_alert = path_in_alert.text
        assert text == text_in_alert, f"expected {text} " \
                                      f"== {text_in_alert}"

    def assert_product_name_in_alert(self):
        self.assert_text_in_alert(ProductPageLocators.NAME_PRODUCT,
                                  ProductPageLocators.NAME_PRODUCT_ALERT_MSG)

    def assert_product_price_in_alert(self):
        self.assert_text_in_alert(ProductPageLocators.PRICE_PRODUCT,
                                  ProductPageLocators.PRICE_PRODUCT_ALERT_MSG)
