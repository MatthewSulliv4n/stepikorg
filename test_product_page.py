import pytest
import time
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


GLOBAL_URL = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo_code',
                         [
                             0, 1, 2, 3, 4, 5, 6,
                             pytest.param(
                                 GLOBAL_URL +
                                 'catalogue/coders-at-work_207/?promo=offer7',
                                 marks=pytest.mark.xfail),
                             8, 9
                         ])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = (GLOBAL_URL + 'catalogue/coders-at-work_207/?promo=offer{}'.format(
        promo_code))
    page = ProductPage(browser, url)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.assert_product_name_in_alert()
    page.assert_product_price_in_alert()


@pytest.mark.smoke
@pytest.mark.regression
def test_guest_cant_see_success_message(browser):
    url = (GLOBAL_URL + 'catalogue/coders-at-work_207/?promo=offer1')
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="its okay for now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = (GLOBAL_URL + 'catalogue/coders-at-work_207/?promo=offer1')
    page = ProductPage(browser, url)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappeared()


@pytest.mark.smoke
@pytest.mark.regression
def test_guest_should_see_login_link_on_product_page(browser):
    url = (GLOBAL_URL + "catalogue/the-city-and-the-stars_95/")
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.smoke
@pytest.mark.regression
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = (GLOBAL_URL + "catalogue/the-city-and-the-stars_95/")
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = (GLOBAL_URL + "catalogue/the-city-and-the-stars_95/")
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()

    page = BasketPage(browser, browser.current_url)
    page.product_should_not_be_present()
    page.should_be_msg_empty_basket()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.url = (GLOBAL_URL + "accounts/login/")
        page = LoginPage(browser, self.url)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "Qwerty1234567")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.url = (GLOBAL_URL + 'catalogue/coders-at-work_207/?promo=offer1')
        page = ProductPage(browser, self.url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.url = (GLOBAL_URL + 'catalogue/coders-at-work_207/?promo=offer1')
        page = ProductPage(browser, self.url)
        page.open()
        page.add_product()
        page.solve_quiz_and_get_code()
        page.assert_product_name_in_alert()
        page.assert_product_price_in_alert()
