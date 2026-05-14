from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class ToolbarComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-toolbar-title-text')
        self.add_button = page.get_by_test_id(f'{identifier}-toolbar-create-course-button')

    def click_add_button(self):
        self.add_button.click()

    def check_visible(self, title):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

    def check_add_button_to_be_enabled(self):
        expect(self.add_button).to_be_visible()
        expect(self.add_button).to_be_enabled()

    def check_add_button_to_be_disabled(self):
        expect(self.add_button).to_be_visible()
        expect(self.add_button).to_be_disabled()