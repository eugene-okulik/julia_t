from playwright.sync_api import Page, expect


def test_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role('link', name="Form Authentication").click()
    page.get_by_role('textbox', name='username').fill('username')
    page.get_by_role("textbox", name="password").fill('password')
    page.get_by_role("button").click()


def test_fill_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder("First Name").fill("Username")
    page.get_by_placeholder("Last Name").fill("Lastname")
    page.locator("#userEmail").fill("test@test.com")
    page.locator("#gender-radio-2").click()
    page.locator("#userNumber").fill("0566667865")
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").select_option(label="March")
    page.locator(".react-datepicker__year-select").select_option(label="1990")
    page.locator(
        ".react-datepicker__day--025:not(.react-datepicker__day--outside-month)"
    ).click()
    page.locator("#subjectsInput").fill("Maths")
    page.get_by_role("option", name="Maths").click()
    page.locator("#subjectsInput").fill("En")
    page.get_by_role("option", name="English").click()
    page.locator("#hobbies-checkbox-3").click()
    page.get_by_placeholder("Current Address").fill("my test address 0123111")
    page.locator("#react-select-3-input").fill("Haryana")
    page.locator("#react-select-3-input").press("Enter")
    page.locator("#react-select-4-input").fill("Karnal")
    page.locator("#react-select-4-input").press("Enter")
    page.get_by_role("button", name="Submit").click()
