from .base_page import BasePage
from locators.prodobro_locators import ProDobroLocators
from assertions.assertions import Assertions

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = ProDobroLocators()
        self.assertions = Assertions(page)
        self.base_url = "https://prodobro.ru/"
        self.funds_button = page.get_by_role("link", name="Фонды")

    def click_funds_link(self):
        self.page.get_by_role("link", name=self.locators.FUNDS_LINK).click()
