from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
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
    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    # Открываем браузер, используем контекст с предыдущего входа, открываем новую страницу в рамках контекста
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    # Переходим на страницу с курсами
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверяем наличие текста Courses
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_have_text('Courses')

    # Проверяем наличие текста There is no results
    there_is_no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(there_is_no_results_text).to_have_text('There is no results')

    # Проверяем наличие иконки пустого списка курсов
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверяем наличие текста
    empty_view_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_text).to_have_text('Results from the load test pipeline will be displayed here')




