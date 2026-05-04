import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_displaying(page, dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page_with_state.navbar.check_visible(name='username')
    dashboard_page_with_state.sidebar.check_visible()