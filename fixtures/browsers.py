from playwright.sync_api import expect, Playwright, Page
import pytest

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    # Открываем браузер, создаем новый контекст, открываем новую страницу в рамках контекста
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('test@test.ru')

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Заполняем поле password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку регистрации
    reg_btn = page.get_by_test_id('registration-page-registration-button')
    reg_btn.click()

    # Сохраняем состояние браузера
    context.storage_state(path='../browser-state.json')
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Открываем браузер, используем контекст фикстуры initialize_browser_state, открываем новую страницу в рамках контекста
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()

@pytest.fixture
def chromium_page(playwright: Playwright):
    # Открываем браузер, создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()