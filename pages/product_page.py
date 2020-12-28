from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_add_to_cart_message()
        self.should_equal_name_of_added_product_and_message()
        #self.should_cost_of_cart_message()
        self.should_equal_cost_of_cart_and_cost_of_product()

    def should_not_to_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_TEXT), 'Success text about added product to cart is here, but should not be'

    def should_add_to_cart_message(self):
        cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_link.click()
        self.solve_quiz_and_get_code()

    def should_equal_name_of_added_product_and_message(self):
        text = self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT).text
        success_text = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT).text
        assert text == success_text, 'Text not in success text'

    def should_cost_of_cart_message(self):
        text = 'Стоимость корзины теперь составляет'
        cost_of_cart_text = self.browser.find_element(*ProductPageLocators.COST_MESSAGE).text
        assert text in cost_of_cart_text, 'Text not in total cost of cart message'

    def should_equal_cost_of_cart_and_cost_of_product(self):
        total_cost = self.browser.find_element(*ProductPageLocators.TOTAL_COST).text
        cost_of_product = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT).text
        assert total_cost == cost_of_product, 'Prices of cart and of product is not equal'
