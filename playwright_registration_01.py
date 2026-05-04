from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Заполняем поле email
    email_input = page.locator("//label[text()='Email']")
    expect(email_input).to_be_visible()

    # Заполняем поле пароль
    password_input = page.locator("//label[text()='Password']")
    expect(password_input).to_be_visible()

    # Нажимаем на кнопку Login
    reg_btn = page.get_by_test_id('login-page-registration-link')
    expect(reg_btn).to_be_enabled()
    reg_btn.click()

    # Проверяем наличие поля email
    email_input = page.locator("//label[text()='Email']")
    expect(email_input).to_be_visible()

    # Проверяем наличие поля Username
    username_input = page.locator("//label[text()='Username']")
    expect(username_input).to_be_visible()

    # Проверяем наличие поля Password
    password_input = page.locator("//label[text()='Password']")
    expect(password_input).to_be_visible()

    # Проверяем наличие кнопки регистрации
    reg_btn = page.get_by_test_id('registration-page-registration-button')
    expect(reg_btn).to_be_visible()