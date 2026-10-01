from playwright.sync_api import expect
from test_UI_tanayno.pages.base_page import BasePage


breadcrumb_title_loc = "span[class='d-inline-block']"
custom_legs_checkbox_loc = "div[class='flex-column mb-3'] label[for='1-7']"
custom_item_loc = "a.text-primary.text-decoration-none"
item_loc = "(//td[@class='oe_product'])[1]"
add_to_cart_loc = "a[aria-label='Shopping cart']"
continue_shopping_btn = "div.modal.o_legacy_dialog button.btn.btn-secondary"


class CatalogCatPage(BasePage):
    page_url = 'shop/category/desks-1'

    def check_breadcrumbs(self, text):
        breadcrumb_title = self.find(breadcrumb_title_loc)
        expect(breadcrumb_title).to_have_text(text)

    def check_custom_legs(self, text):
        custom_legs_checkbox = self.find(custom_legs_checkbox_loc)
        custom_legs_checkbox.click()

        customized_item = self.page.get_by_text(text, exact=True)
        expect(customized_item).to_have_text(text)

    def add_to_cart(self):
        item = self.find(item_loc)
        # наводим мышь на товар
        item.hover()
        # ищем иконку корзины внутри товара
        add_to_cart = item.locator(add_to_cart_loc)
        # добавляем в корзину
        add_to_cart.click()
        # продолжить покупки
        continue_shopping = self.find(continue_shopping_btn)
        continue_shopping.click()
