from page_objects.MainPage import MainPage
from page_objects.AuthorizationPage import AuthorizationPage


def test_authorization_valid(browser, user_name_valid, password_valid):
    MainPage(browser).go_to_authorization_form()
    AuthorizationPage(browser).input_username_into_authorization_form(user_name_valid)
    AuthorizationPage(browser).click_confirmation_button()
    AuthorizationPage(browser).input_password_into_authorization_form(password_valid)
    AuthorizationPage(browser).click_confirmation_button()
    assert AuthorizationPage(browser).get_text_of_authorized_user() == user_name_valid
