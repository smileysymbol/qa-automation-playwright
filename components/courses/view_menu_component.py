from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class ViewMenuComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.edit_button = page.get_by_test_id(f'{identifier}-edit-menu-item')
        self.delete_button = page.get_by_test_id(f'{identifier}-delete-menu-item')

    def check_visible(self, index: int):
        menu_button = self.page.get_by_test_id('course-view-menu-button').nth(index)

        menu_button.click()

        expect(self.edit_button).to_be_visible()
        expect(self.edit_button).to_be_enabled()

        expect(self.delete_button).to_be_visible()
        expect(self.delete_button).to_be_enabled()
