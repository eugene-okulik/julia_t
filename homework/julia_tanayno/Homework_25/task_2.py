from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def send_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("julia")
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("surname")
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("test@test.com")
    gender = driver.find_element(By.ID, "gender-radio-2")
    gender.click()
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")
    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()

    year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year.select_by_value("2000")

    month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month.select_by_value("2")

    day = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--008")
    day.click()

    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Biology")
    subjects.send_keys(Keys.ENTER)

    hobby = driver.find_element(By.ID, "hobbies-checkbox-3")
    hobby.click()

    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("test address")

    state = driver.find_element(By.ID, "react-select-3-input")

    state.send_keys("Rajasthan")
    state.send_keys(Keys.ENTER)

    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys("Jaipur")
    city.send_keys(Keys.ENTER)

    # прокрутили страницу
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

    for row in rows:
        print(row.text)
    driver.quit()


send_form()
