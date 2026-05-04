from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.empty_courses_list_text = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_description_text = page.get_by_test_id(
            'courses-list-empty-view-description-text'
        )
        self.add_course_button = page.get_by_test_id('AddIcon')
        self.edit_course_button = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_course_button = page.get_by_test_id('course-view-delete-menu-item')


    def check_visible_courses_title(self):
        expect(self.courses_title).to_have_text('Courses')

    def check_there_is_no_results_text(self):
        expect(self.empty_courses_list_text).to_have_text('There is no results')

    def check_empty_view_icon(self):
        expect(self.empty_view_icon).to_be_visible()

    def check_empty_view_description_text(self):
        expect(self.empty_view_description_text).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.add_course_button).to_be_visible()
        expect(self.add_course_button).to_be_enabled()

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            estimated_time: str,
            max_score: str,
            min_score: str
    ):

        course_title = self.page.get_by_test_id('course-widget-title-text').nth(index)
        course_max_score = self.page.get_by_test_id('course-max-score-info-row-view-text').nth(index)
        course_min_score = self.page.get_by_test_id('course-min-score-info-row-view-text').nth(index)
        course_estimated_time = self.page.get_by_test_id('course-estimated-time-info-row-view-text').nth(index)

        expect(course_title).to_be_visible()
        expect(course_title).to_have_text(title)

        expect(course_max_score).to_be_visible()
        expect(course_max_score).to_have_text(f'Max score: {max_score}')

        expect(course_min_score).to_be_visible()
        expect(course_min_score).to_have_text(f'Min score: {min_score}')

        expect(course_estimated_time).to_be_visible()
        expect(course_estimated_time).to_have_text(f'Estimated time: {estimated_time}')

    def check_menu_course(self, index: int):
        course_menu_button = self.page.get_by_test_id('course-view-menu-button').nth(index)

        course_menu_button.click()

        expect(self.edit_course_button).to_be_visible()
        expect(self.edit_course_button).to_be_enabled()

        expect(self.delete_course_button).to_be_visible()
        expect(self.delete_course_button).to_be_enabled()
