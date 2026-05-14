import allure
from playwright.sync_api import Page, expect
from components.courses.empty_view_component import EmptyViewComponent
from components.courses.toolbar_component import ToolbarComponent
from components.courses.upload_widget_component import UploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.toolbar_component = ToolbarComponent(page, identifier='create-course')
        self.upload_widget_component = UploadWidgetComponent(page, identifier='create-course-preview')

        self.course_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.course_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.add_exercises_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        with allure.step(
                f'Fill the create course form with data: {title}, {estimated_time}, '
                f'{description}, {max_score}, {min_score}'
        ):

            self.course_title.fill(title)
            expect(self.course_title).to_have_value(title)

            self.course_estimated_time.fill(estimated_time)
            expect(self.course_estimated_time).to_have_value(estimated_time)

            self.course_description.fill(description)
            expect(self.course_description).to_have_value(description)

            self.max_score.fill(max_score)
            expect(self.max_score).to_have_value(max_score)

            self.min_score.fill(min_score)
            expect(self.min_score).to_have_value(min_score)

    def check_visible_create_course_form(self):
        with allure.step('Check create course form is visible'):
            expect(self.course_title).to_be_visible()
            expect(self.course_title).to_have_text('')

            expect(self.course_estimated_time).to_be_visible()
            expect(self.course_estimated_time).to_have_text('')

            expect(self.course_description).to_be_visible()
            expect(self.course_description).to_have_text('')

            expect(self.max_score).to_be_visible()
            expect(self.max_score).to_have_value('0')

            expect(self.min_score).to_be_visible()
            expect(self.min_score).to_have_value('0')

    def check_visible_exercises_title(self, title: str):
        with allure.step(f'Check exercises title {title} is visible'):
            expect(self.exercises_title).to_be_visible()
            expect(self.exercises_title).to_have_text(title)

    def check_visible_create_exercise_button(self):
        with allure.step('Check create exercise button is visible'):
            expect(self.add_exercises_button).to_be_visible()


