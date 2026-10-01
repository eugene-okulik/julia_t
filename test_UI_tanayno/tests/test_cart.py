def test_header_title(cart_page):
    cart_page.open_page()
    cart_page.check_cart_title_is('Order overview')

def test_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.check_cart_alert('Your cart is empty!')

def test_delete_from_cart(cart_page, catalog_category_page):
    catalog_category_page.open_page()
    catalog_category_page.add_to_cart()
    catalog_category_page.check_cart_quantity(1)
    cart_page.open_page()
    cart_page.delete_item_from_cart()
    cart_page.check_cart_alert('Your cart is empty!')

def test_change_item_quantity(cart_page, catalog_category_page):
    catalog_category_page.open_page()
    catalog_category_page.add_to_cart()
    catalog_category_page.check_cart_quantity(1)
    cart_page.open_page()
    cart_page.change_quantity()
    cart_page.check_item_price("1,500.00")
