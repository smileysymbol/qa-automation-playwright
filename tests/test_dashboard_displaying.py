import pytest, allure
from pages.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.dashboard
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.Dashboard)
@allure.story(AllureStory.Dashboard)
class TestDashboard:
    @allure.title('Check dashboard is displaying')
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        dashboard_page_with_state.navbar.check_visible(name='username')
        dashboard_page_with_state.sidebar.check_visible()