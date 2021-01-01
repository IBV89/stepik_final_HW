from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASCET_LINK = (By.XPATH, '//a[contains (text(), "View basket")]')
    USER_ICON = (By.CSS_SELECTOR, 'i.icon-user')


class CartPageLocators():
    CART_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner')
    CART_FORM = (By.CSS_SELECTOR, '#basket_formset')
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner>p')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    SUCCESS_REGISTER_TEXT = (By.CSS_SELECTOR, 'div.alert-success>div.alertinner.wicon')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_TEXT = (By.CSS_SELECTOR, 'div:nth-child(1)>div.alertinner>strong')
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main>h1')
    COST_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner>p:nth-child(1)')
    TOTAL_COST = (By.CSS_SELECTOR, 'div.alertinner>p:nth-child(1)>strong')
    COST_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
