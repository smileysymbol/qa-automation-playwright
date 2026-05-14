import pytest, allure
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.registration
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.Authentication)
@allure.story(AllureStory.Registration)
class TestRegistration:
    @allure.title('Check successful registration')
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):

        registration_page.visit(
            url='https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        )
        registration_page.fill_registration_form(
            email='user.name@gmail.com',
            username='username',
            password='password'
        )
        registration_page.click_registration_button()
        dashboard_page.check_visible_text()