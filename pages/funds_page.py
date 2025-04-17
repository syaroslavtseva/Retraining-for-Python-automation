from .base_page import BasePage
from locators.prodobro_locators import ProDobroLocators
from assertions.assertions import Assertions

class FundsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = ProDobroLocators()
        self.assertions = Assertions(page)
        self.input_field = page.locator("css=.relative.w-full input")
        self.batton_klyuch_dobra = page.get_by_text("Ключ добра")
        
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
    
