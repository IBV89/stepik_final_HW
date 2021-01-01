from .base_page import BasePage
from .locators import LoginPageLocators
import re
import time
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        is_login_in_url = re.findall('login', current_url)[-1]
        assert is_login_in_url, 'Not found "login" string in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Form for login not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Form for registration not found'

    def register_new_user(self, email=str(int(time.time())) + '@mail.ru', password='12345678g'):
        # email = str(time.time()) + '@mail.ru'
        email_imput = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_imput.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_input.send_keys(password)
        confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        confirm_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        button.click()
