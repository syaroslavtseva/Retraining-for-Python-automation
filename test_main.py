from playwright.sync_api import Playwright, sync_playwright,expect
from steps.prodobro_steps import ProDobroSteps


def test(page):
    steps = ProDobroSteps(page)
    steps.navigate_and_check_funds()
    steps.search_and_select_fund()
    steps.check_viewport_sizes()

