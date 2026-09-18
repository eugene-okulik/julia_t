from playwright.sync_api import Page, expect, Route
import json


def test_popup_title(page: Page):
    changed_title = 'яблокофон 18 про'

    def change_title(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][1]["familyTypes"][0]["productName"] = changed_title
        # преобразовать body в json
        body = json.dumps(body)
        # response берем как был, а в body подставляем наш измененный body
        route.fulfill(
            response=response,
            body=body
        )

    # обработка запроса отдается функции change_title
    page.route("**/digital-mat**", change_title)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.get_by_role("heading", name="iPhone 18 Pro & iPhone 18 Pro Max - NEW").click()
    title_result = page.locator('[data-autom="DigitalMat-overlay-header-1-0"]')
    expect(title_result).to_have_text(changed_title)
