from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_course_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.create_course_empty_view_text = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.create_course_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        self.upload_image_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_image_text = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_button = page.get_by_test_id('create-course-preview-image-upload-widget-input')
        self.image_preview = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        self.course_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.course_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.add_exercises_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        self.empty_exercises_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.empty_exercises_text = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.empty_exercises_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')

    def upload_preview_image(self):
        self.upload_image_button.set_input_files('./testdata/files/image.png')

    def click_create_course_button(self):
        self.create_course_button.click()

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
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

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        expect(self.create_course_button).to_be_disabled()

    def check_visible_image_preview_empty_view(self):
        expect(self.create_course_empty_view_icon).to_be_visible()

        expect(self.create_course_empty_view_text).to_be_visible()
        expect(self.create_course_empty_view_text).to_have_text('No image selected')

        expect(self.create_course_empty_view_description).to_be_visible()
        expect(self.create_course_empty_view_description).to_have_text('Preview of selected image will be displayed here')

    def check_visible_image_upload_view(self, is_image_uploaded=False):
        expect(self.upload_image_icon).to_be_visible()

        expect(self.upload_image_text).to_be_visible()
        expect(self.upload_image_text).to_have_text('Tap on "Upload image" button to select file')

        expect(self.upload_image_button).to_be_visible()

        if is_image_uploaded:
            expect(self.image_preview).to_be_visible()

    def check_visible_create_course_form(self):
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

    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.add_exercises_button).to_be_visible()

    def check_visible_exercises_empty_view(self):
        expect(self.empty_exercises_icon).to_be_visible()

        expect(self.empty_exercises_text).to_be_visible()
        expect(self.empty_exercises_text).to_have_text('There is no exercises')

        expect(self.empty_exercises_description).to_be_visible()
        expect(self.empty_exercises_description).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )



