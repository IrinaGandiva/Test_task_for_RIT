from page_objects.Base import BasePage
from selenium.webdriver.common.by import By


class AuthorizationPage(BasePage):
    """Страница авторизации"""

    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    CONFIRMATION_BUTTON = (By.XPATH, "//input[@type = 'submit']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    USER_INFO = (By.CSS_SELECTOR, ".user-info")

    def input_username_into_authorization_form(self, name):
        self._input(*self.USERNAME_FIELD, value=name)
        return self

    def click_confirmation_button(self):
        self._click(*self.CONFIRMATION_BUTTON)

    def input_password_into_authorization_form(self, password):
        self._input(*self.PASSWORD_FIELD, value=password)
        return self

    def get_text_of_authorized_user(self):
        return self._get_element_text(*self.USER_INFO)
