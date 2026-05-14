from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.view_menu_component import ViewMenuComponent


class ViewCardComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, index: int):
        super().__init__(page)

        self.view_menu_component = ViewMenuComponent(page, identifier='courses-list')

        self.course_title = self.page.get_by_test_id(f'{identifier}-widget-title-text').nth(index)
        self.course_max_score = self.page.get_by_test_id(f'{identifier}-max-score-info-row-view-text').nth(index)
        self.course_min_score = self.page.get_by_test_id(f'{identifier}-min-score-info-row-view-text').nth(index)
        self.course_estimated_time = self.page.get_by_test_id(f'{identifier}-estimated-time-info-row-view-text').nth(index)

    def check_visible_course_card(
            self,
            title: str,
            estimated_time: str,
            max_score: str,
            min_score: str
    ):

        expect(self.course_title).to_be_visible()
        expect(self.course_title).to_have_text(title)

        expect(self.course_max_score).to_be_visible()
        expect(self.course_max_score).to_have_text(f'Max score: {max_score}')

        expect(self.course_min_score).to_be_visible()
        expect(self.course_min_score).to_have_text(f'Min score: {min_score}')

        expect(self.course_estimated_time).to_be_visible()
        expect(self.course_estimated_time).to_have_text(f'Estimated time: {estimated_time}')