from playwright.sync_api import Page, Locator
from playwright.sync_api import expect

cart_quantity_loc = ".my_cart_quantity"


class BasePage:
    base_url = "http://testshop.qa-practice.com/"
    # текущий урл для страницы
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def check_cart_quantity(self, expected_quantity):
        cart_quantity = self.find(cart_quantity_loc).first
        expect(cart_quantity).to_have_text(str(expected_quantity))
