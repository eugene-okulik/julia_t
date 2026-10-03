from playwright.sync_api import expect
from test_UI_tanayno.pages.base_page import BasePage

item_title_loc = "h1"
terms_link_loc = "[href='/terms']"
terms_title_loc = "h1"
quantity_field_loc = "input.form-control.quantity"
cart_button_loc = "#add_to_cart_wrap"


class ItemPage(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def check_item_title(self, text):
        item_title = self.find(item_title_loc)
        expect(item_title).to_have_text(text)

    def open_terms_and_conditions(self):
        terms_link = self.find(terms_link_loc)
        terms_link.click()

    def check_terms_page_title(self, expected_title):
        terms_title = self.find(terms_title_loc)
        expect(terms_title).to_have_text(expected_title)

    def enter_quantity(self, quantity):
        quantity_field = self.find(quantity_field_loc)
        quantity_field.clear()
        quantity_field.fill(str(quantity))

    def add_to_cart(self):
        cart_button = self.find(cart_button_loc)
        cart_button.click()
