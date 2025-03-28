from playwright.sync_api import Page, expect

class Assertions:
    def __init__(self, page: Page):
        self.page = page

    def verify_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)

    def verify_input_value(self, locator: str, expected_value: str):
        input_element = self.page.locator(locator)
        expect(input_element).to_have_value(expected_value)

    def print_page_info(self):
        print(f"URL: {self.page.url}, Title: {self.page.title()}")