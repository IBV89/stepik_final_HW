# pytest -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.cart
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_link()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_cart_empty()
    cart_page.should_cart_is_empty_text()



