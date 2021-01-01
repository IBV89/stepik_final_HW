from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_FORM), \
            'Form in cart must be not showing, but it shows'

    def should_cart_is_empty_text(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY_TEXT), \
            'Text for empty basket is not present'
