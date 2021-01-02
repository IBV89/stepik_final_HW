import pytest
# pytest -s test_product_page.py
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time

url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()


@pytest.mark.skip
@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_add_to_cart_message()
    page.should_not_to_be_success_message()


@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_to_be_success_message()


@pytest.mark.skip
@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_add_to_cart_message()
    page.should_be_is_disappeared()


@pytest.mark.any_page_login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_link()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_cart_empty()
    cart_page.should_cart_is_empty_text()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/accounts/login/')
        page.open()
        page.register_new_user(str(int(time.time())) + '@mail.ru', '12345678g')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.should_not_to_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
