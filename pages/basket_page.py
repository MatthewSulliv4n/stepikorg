import pytest
from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_msg_empty_basket(self):
        if "/ru" in self.browser.current_url:
            msg_correct_text = "Ваша корзина пуста Продолжить покупки"
        elif "/en" in self.browser.current_url:
            msg_correct_text = "Your basket is empty. Continue " \
                               "shopping"
        else:
            raise pytest.UsageError(
                "looks like you need to add translation for message in basket")
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG)

        assert msg.text == msg_correct_text, f"expected {msg.text} " \
                                             f"== {msg_correct_text}"

    def product_should_not_be_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT)
