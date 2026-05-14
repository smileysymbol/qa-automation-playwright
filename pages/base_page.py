import re, allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Visit the page {url}'):
            self.page.goto(url)

    def check_url(self, expected_url: str):
        with allure.step(f'Check we visit page with path in url - {expected_url}'):
            expect(self.page).to_have_url(re.compile(fr".*{expected_url}$"))

    def refresh_page(self):
        self.page.reload()