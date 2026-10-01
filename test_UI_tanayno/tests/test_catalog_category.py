def test_breadcrumbs_title(catalog_category_page):
    catalog_category_page.open_page()
    catalog_category_page.check_breadcrumbs('Desks')

def test_custom_legs(catalog_category_page):
    catalog_category_page.open_page()
    catalog_category_page.check_custom_legs('Customizable Desk')

def test_add_to_cart(catalog_category_page):
    catalog_category_page.open_page()
    catalog_category_page.add_to_cart()
    catalog_category_page.check_cart_quantity(1)
