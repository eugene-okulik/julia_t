from playwright.sync_api import BrowserContext
import pytest
from pytest_playwright.pytest_playwright import playwright

from test_UI_tanayno.pages.cart_page import CartPage
from test_UI_tanayno.pages.catalog_category_page import CatalogCatPage
from test_UI_tanayno.pages.item_page import ItemPage

# инициализация страницы
@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def catalog_category_page(page):
    return CatalogCatPage(page)

@pytest.fixture
def item_page(page):
    return ItemPage(page)

@pytest.fixture
# context - запущенный браузер
def page(context: BrowserContext, playwright):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page

