from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator("//input[@id=':r0:']")
        self.username_input = page.locator("//input[@id=':r1:']")
        self.password_input = page.locator("//input[@id=':r2:']")
        self.reg_button = page.locator("//button[@id='registration-page-registration-button']")
        self.login_button = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email, username, password):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        self.reg_button.click()

    def click_login_button(self):
        self.login_button.click()


