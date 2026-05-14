from playwright.sync_api import Page, expect

from components.courses.empty_view_component import EmptyViewComponent
from components.courses.view_card_component import ViewCardComponent
from components.courses.view_menu_component import ViewMenuComponent
from components.courses.toolbar_component import ToolbarComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar_component = ToolbarComponent(page, identifier='courses-list')
        self.empty_view_component = EmptyViewComponent(page, identifier='courses-list')
        self.view_menu_component = ViewMenuComponent(page, identifier='course-view')
        self.view_card_component = ViewCardComponent(page, identifier='course', index=0)