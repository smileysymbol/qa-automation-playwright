from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле email
    email_input = page.locator("//input[@id=':r0:']")
    email_input.fill('user.name@gmail.com')

    # Заполняем поле username
    email_input = page.locator("//input[@id=':r1:']")
    email_input.fill('username')

    # Заполняем поле password
    email_input = page.locator("//input[@id=':r2:']")
    email_input.fill('password')

    # Нажимаем на кнопку регистрации
    reg_button = page.locator("//button[@id='registration-page-registration-button']")
    reg_button.click()

    # Проверяем, что мы на странице дашборда
    dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_text).to_have_text('Dashboard')