import re
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def check_url(self, expected_url: str):
        expect(self.page).to_have_url(re.compile(fr".*{expected_url}$"))