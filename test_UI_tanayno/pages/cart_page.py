from playwright.sync_api import expect
from test_UI_tanayno.pages.base_page import BasePage

cart_page_title_loc = "h3"
empty_cart_alert_loc = "div.js_cart_lines.alert.alert-info"
remove_from_cart_btn_loc = "[aria-label='Remove from cart']"
plus_item_loc = "i.fa.fa-plus.position-relative.z-index-1"
price_item_loc = "span[data-oe-type='monetary'] span[class='oe_currency_value']"

class CartPage(BasePage):
    page_url = 'shop/cart'

    def check_cart_title_is(self, text):
        cart_title = self.find(cart_page_title_loc)
        expect(cart_title).to_have_text(text)


    def check_cart_alert(self, expected_cart_alert):
        empty_cart_alert = self.find(empty_cart_alert_loc)
        expect(empty_cart_alert).to_have_text(expected_cart_alert)


    def delete_item_from_cart(self):
        remove_from_cart_btn = self.find(remove_from_cart_btn_loc)
        expect(remove_from_cart_btn).to_be_visible()
        remove_from_cart_btn.click()

    def change_quantity(self):
        plus_item = self.find(plus_item_loc)
        plus_item.click()

    def check_item_price(self, expected_price):
        price_item = self.find(price_item_loc)
        expect(price_item).to_have_text(expected_price)
