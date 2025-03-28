from playwright.sync_api import Playwright, sync_playwright,expect
from pages.prodobro_page import ProDobroPage
from steps.prodobro_steps import ProDobroSteps

def test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    try:
        steps = ProDobroSteps(page)
        steps.navigate_and_check_funds()
        steps.search_and_select_fund()
        steps.check_viewport_sizes()
    finally:
        #page.close()
        context.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        test(playwright)