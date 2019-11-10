import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


GLOBAL_URL = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.smoke
@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, GLOBAL_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


@pytest.mark.smoke
@pytest.mark.regression
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, GLOBAL_URL)
    page.open()
    page.go_to_basket()

    page = BasketPage(browser, browser.current_url)
    page.product_should_not_be_present()
    page.should_be_msg_empty_basket()
