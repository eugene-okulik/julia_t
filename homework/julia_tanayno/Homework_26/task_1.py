from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_check_adding_item_to_cart_in_new_tab(driver):
    driver.get("http://testshop.qa-practice.com/")
    item = driver.find_element(By.CSS_SELECTOR, "[content='Customizable Desk']")
    actions = ActionChains(driver)
    actions.key_down(Keys.COMMAND)
    actions.click(item)
    actions.key_up(Keys.COMMAND)
    actions.perform()

    # получили список табов
    tabs = driver.window_handles

    # переключились на 2 таб
    driver.switch_to.window(tabs[1])

    # добавляем в корзину
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_to_cart"))
    )
    # add_to_cart.click() - почему-то не срабатывает
    ActionChains(driver).move_to_element(add_to_cart).click().perform()

    # ждем поп-ап
    WebDriverWait(driver, 6).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal.o_legacy_dialog"))
    )
    # продолжить покупки
    continue_shopping = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal.o_legacy_dialog button.btn.btn-secondary"))
    )
    continue_shopping.click()

    # ждем пока отобразится иконка с количеством товара
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".my_cart_quantity"))
    )

    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.CSS_SELECTOR, "[href='/shop/cart']").click()
    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".d-inline.align-top.h6.fw-bold")
        )
    )
    assert result.text.startswith("Customizable Desk")


def test_check_adding_item_to_cart(driver):
    driver.get("http://testshop.qa-practice.com/")
    item = driver.find_element(By.XPATH, "//tbody/tr[1]/td[@data-name='Product'][1]")
    product_name = item.find_element(
        By.CSS_SELECTOR, "a.text-primary.text-decoration-none"
    ).text
    image = item.find_element(By.TAG_NAME, "img")
    actions = ActionChains(driver)
    actions.move_to_element(image).perform()
    cart = item.find_element(By.CSS_SELECTOR, ".fa-shopping-cart")
    actions.move_to_element(cart).click().perform()

    # ждем поп-ап
    WebDriverWait(driver, 6).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal.o_legacy_dialog"))
    )
    added_item = driver.find_element(
        By.CSS_SELECTOR, "tr.js_product.in_cart.main_product strong.product-name.product_display_name"
    )

    assert product_name in added_item.text
