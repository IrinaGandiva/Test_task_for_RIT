from page_objects.RegistrationPage import RegistrationPage

from page_objects.MainPage import MainPage


def test_registration_valid_user_without_captcha(browser, user_name_valid, email_valid):
    MainPage(browser).go_to_registration_form()
    RegistrationPage(browser).input_name_to_registration_form(user_name_valid)
    RegistrationPage(browser).input_email_to_registration_form(email_valid)
    RegistrationPage(browser).click_to_submit_button()
    # для регистрации требуется ввод captcha, поэтому в тесте проверяется вывод ошибки
    assert RegistrationPage(browser).get_text_of_error_registration_without_captcha() == 'APPLICATION ERROR #1904'
