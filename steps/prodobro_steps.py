from pages.prodobro_page import ProDobroPage

class ProDobroSteps:
    def __init__(self, page):
        self.page = ProDobroPage(page)

    def navigate_and_check_funds(self):
        self.page.navigate(self.page.base_url)
        self.page.assertions.verify_url(self.page.base_url)
        self.page.assertions.print_page_info()
        self.page.reload_page()
        self.page.click_funds_link()
        self.page.assertions.print_page_info()

    def search_and_select_fund(self):
        self.page.click_animals_button()
        input_field = self.page.fill_search_input("ввод")
        self.page.assertions.verify_input_value(self.page.locators.SEARCH_INPUT, "ввод")
        self.page.clear_search_input()
        print(self.page.get_cookies())
        self.page.fill_search_input("кл")
        self.page.click_klyuch_dobra()
        self.page.assertions.print_page_info()
        self.page.click_fund_site()

    def check_viewport_sizes(self):
        self.page.set_viewport_size(1920, 1080)
        self.page.set_viewport_size(320, 480)