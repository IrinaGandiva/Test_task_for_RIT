from page_objects.Base import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    """Страница регистрации"""

    NAME_FIELD = (By.XPATH, "//*[@id='username']")
    EMAIL_FIELD = (By.XPATH, "//*[@id='email-field']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type ='submit']")
    ERROR_TITLE_WITHOUT_CAPTCHA = (By.XPATH, "//p[text()='APPLICATION ERROR #1904']")

    def input_name_to_registration_form(self, name):
        self._input(*self.NAME_FIELD, value=name)
        return self

    def input_email_to_registration_form(self, email):
        self._input(*self.EMAIL_FIELD, value=email)
        return self

    def click_to_submit_button(self):
        self._click(*self.SUBMIT_BUTTON)
        return self

    def get_text_of_error_registration_without_captcha(self):
        return self._get_element_text(*self.ERROR_TITLE_WITHOUT_CAPTCHA)
