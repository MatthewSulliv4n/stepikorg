from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_code',
                         [
                             0, 1, 2, 3, 4, 5, 6,
                             pytest.param(
                                 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                                 marks=pytest.mark.xfail),
                             8, 9
                         ])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = ('http://selenium1py.pythonanywhere.com/catalogue/'
           'coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, url)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.assert_product_name_in_alert()
    page.assert_product_price_in_alert()
