from .base_page import BasePage
from locators.prodobro_locators import ProDobroLocators
from assertions.assertions import Assertions
     
class ProDobroPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = ProDobroLocators()
        self.assertions = Assertions(page)
        self.base_url = "https://prodobro.ru/"

    def click_funds_link(self):
        self.page.get_by_role("link", name=self.locators.FUNDS_LINK).click()

    def click_animals_button(self):
        self.page.evaluate(self.locators.ANIMALS_BUTTON_SCRIPT)

    def fill_search_input(self, text: str):
        input_field = self.page.locator(self.locators.SEARCH_INPUT)
        input_field.fill(text)
        return input_field

    def clear_search_input(self):
        self.page.locator(self.locators.SEARCH_INPUT).clear()

    def click_klyuch_dobra(self):
        self.page.get_by_text(self.locators.KLYUCH_DOBRA_TEXT).click()
    def click_fund_site(self):
        self.page.get_by_text(self.locators.FUND_SITE_LINK).click()
