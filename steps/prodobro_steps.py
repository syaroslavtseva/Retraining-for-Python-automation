from pages.home_page import HomePage
from pages.funds_page import FundsPage
from pages.foundations_page import FoundationsPage

class ProDobroSteps:
    def __init__(self, page):
        self.home_page = HomePage(page)
        self.funds_page = FundsPage(page)
        self.foundations_page = FoundationsPage(page)

    def navigate_and_check_funds(self):
        self.home_page.navigate(self.home_page.base_url)
        self.home_page.assertions.verify_url(self.home_page.base_url)
        self.home_page.assertions.print_page_info()
        self.home_page.reload_page()
        self.home_page.click_funds_link()
        self.home_page.assertions.print_page_info()

    def search_and_select_fund(self):
        self.funds_page.click_animals_button()
        input_field = self.funds_page.fill_search_input("ввод")
        self.funds_page.assertions.verify_input_value(self.funds_page.locators.SEARCH_INPUT, "ввод")
        self.funds_page.clear_search_input()
        print(self.funds_page.get_cookies())
        self.funds_page.fill_search_input("кл")
        self.funds_page.click_klyuch_dobra()
        self.funds_page.assertions.print_page_info()
        self.foundations_page.click_fund_site()

    def check_viewport_sizes(self):
        self.foundations_page.set_viewport_size(1920, 1080)
        self.foundations_page.set_viewport_size(320, 480)
