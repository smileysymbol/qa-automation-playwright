import pytest, allure
from pages.login_page import LoginPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.parametrize('email, password', [('user.name@gmail.com', 'password'), ('user.name@gmail.com', '  '), ('  ', 'password')])
@pytest.mark.authorization
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.Authentication)
@allure.story(AllureStory.Authorization)
class TestAuthorization:
    @allure.title('Check authorization with wrong email or password')
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.fill_authorization_form(email, password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()


