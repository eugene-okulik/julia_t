from selenium import webdriver
from selenium.webdriver.common.by import By


def find_and_print_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_field = driver.find_element(By.ID, 'id_text_string')
    text_field.send_keys("Hello")
    text_field.submit()
    result = driver.find_element(By.ID, 'result-text').text
    print(result)
    driver.quit()


find_and_print_element()
