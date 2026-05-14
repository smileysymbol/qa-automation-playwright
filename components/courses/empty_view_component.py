from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title_text = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.description_text = page.get_by_test_id(
            f'{identifier}-empty-view-description-text'
        )

    def check_visible(self, title: str, description: str):
        expect(self.icon).to_be_visible()

        expect(self.title_text).to_be_visible()
        expect(self.title_text).to_have_text(title)

        expect(self.description_text).to_be_visible()
        expect(self.description_text).to_have_text(description)

