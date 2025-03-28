from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def navigate(self, url: str):
        # Перейти по url
        self.page.goto(url)
    def reload_page(self):
        # Обновлять страницу
        self.page.reload()
    def get_cookies(self):
        # Выводить cookies
        return self.page.context.cookies()
    def set_viewport_size(self, width: int, height: int):
        # Менять размеры области просмотра
        self.page.set_viewport_size({"width": width, "height": height})
