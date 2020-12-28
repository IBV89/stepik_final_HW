# pytest -v --tb=line --language=en test_login_page.py
from .pages.login_page import LoginPage
link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

def test_should_be_login_forn(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
def test_should_be_registration_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
def test_should_be_correct_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()