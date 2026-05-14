import pytest, allure
from pages.courses_list_page import CoursesPage
from pages.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.courses
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.Courses)
@allure.story(AllureStory.Courses)
class TestCourses:
        @allure.title('Check courses list view')
        def test_empty_courses_list(self, courses_page: CoursesPage):
                courses_page.visit(
                        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
                )

                courses_page.navbar.check_visible(name='username')
                courses_page.sidebar.check_visible()

                courses_page.check_url(expected_url='/#/courses')
                courses_page.toolbar_component.check_visible(title='Courses')
                courses_page.empty_view_component.check_visible(title='There is no results', description='Results from the load test pipeline will be displayed here')

        @allure.title('Check course card, edit menu and possibility of creating course')
        def test_create_courses_list(self, courses_page: CoursesPage, create_course_page: CreateCoursePage):
                create_course_page.visit(
                        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
                )

                create_course_page.check_url(expected_url='/#/courses/create')
                create_course_page.toolbar_component.check_visible(title='Create course')
                create_course_page.toolbar_component.check_add_button_to_be_disabled()
                create_course_page.preview_empty_view.check_visible(
                        title='No image selected',
                        description='Preview of selected image will be displayed here'
                )

                create_course_page.check_visible_create_course_form()

                create_course_page.check_visible_exercises_title(title='Exercises')
                create_course_page.check_visible_create_exercise_button()
                create_course_page.exercises_empty_view.check_visible(
                        title='There is no exercises',
                        description='Click on "Create exercise" button to create new exercise'
                )

                create_course_page.upload_widget_component.upload_preview_image()
                create_course_page.upload_widget_component.check_visible_upload_widget(
                        title='Tap on "Upload image" button to select file',
                        description='Recommended file size 540X300',
                        is_image_uploaded=True
                )

                create_course_page.fill_create_course_form(
                        title="Playwright",
                        estimated_time="2 weeks",
                        description="Playwright",
                        max_score='100',
                        min_score='10'
                )
                create_course_page.toolbar_component.click_add_button()

                courses_page.check_url(expected_url='/#/courses')
                courses_page.toolbar_component.check_visible(title='Courses')
                courses_page.toolbar_component.check_add_button_to_be_enabled()

                courses_page.view_card_component.check_visible_course_card(
                        title="Playwright",
                        estimated_time="2 weeks",
                        max_score='100',
                        min_score='10'
                )

                courses_page.view_menu_component.check_visible(index=0)





