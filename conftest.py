import pytest
from playwright.sync_api import Playwright, sync_playwright,expect

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield browser
    context.close()
    browser.close()
    