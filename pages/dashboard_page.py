from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible_text(self):
        expect(self.dashboard_text).to_be_visible()
        expect(self.dashboard_text).to_have_text('Dashboard')
