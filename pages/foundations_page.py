from .base_page import BasePage
from locators.prodobro_locators import ProDobroLocators
from assertions.assertions import Assertions

class FoundationsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = ProDobroLocators()
        self.assertions = Assertions(page)
        self.batton_foundations_website= page.get_by_role("link", name="Сайт фонда")
    def click_fund_site(self):
        self.page.get_by_text(self.locators.FUND_SITE_LINK).click()
    
