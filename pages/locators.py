from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_TEXT = (By.CSS_SELECTOR, 'div:nth-child(1)>div.alertinner>strong')
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main>h1')
    COST_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner>p:nth-child(1)')
    TOTAL_COST = (By.CSS_SELECTOR, 'div.alertinner>p:nth-child(1)>strong')
    COST_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
