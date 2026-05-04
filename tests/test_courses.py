import pytest
from pages.courses_list_page import CoursesPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_page: CoursesPage):
        courses_page.visit(
                'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        )

        courses_page.check_url(expected_url='/#/courses')
        courses_page.check_visible_courses_title()
        courses_page.check_empty_view_icon()
        courses_page.check_empty_view_description_text()
        courses_page.check_there_is_no_results_text()

@pytest.mark.regression
@pytest.mark.courses
def test_create_courses_list(courses_page: CoursesPage, create_course_page: CreateCoursePage):
        create_course_page.visit(
                'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )

        create_course_page.check_url(expected_url='/#/courses/create')
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.check_visible_image_upload_view()
        create_course_page.check_visible_create_course_form()
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.upload_preview_image()
        create_course_page.check_visible_image_upload_view()
        create_course_page.fill_create_course_form(
                title="Playwright",
                estimated_time="2 weeks",
                description="Playwright",
                max_score='100',
                min_score='10'
        )
        create_course_page.click_create_course_button()

        courses_page.check_url(expected_url='/#/courses')
        courses_page.check_visible_courses_title()
        courses_page.check_visible_create_course_button()

        courses_page.check_visible_course_card(
                index=0,
                title="Playwright",
                estimated_time="2 weeks",
                max_score='100',
                min_score='10'
        )

        courses_page.check_menu_course(index=0)





