def test_item_title(item_page):
    item_page.open_page()
    item_page.check_item_title('Office Design Software')

def test_terms_page_is_opened(item_page):
    item_page.open_page()
    item_page.open_terms_and_conditions()
    item_page.check_terms_page_title('STANDARD TERMS AND CONDITIONS OF SALE')

def test_add_to_cart(item_page):
    item_page.open_page()
    item_page.enter_quantity(3)
    item_page.add_to_cart()
    item_page.check_cart_quantity(3)
