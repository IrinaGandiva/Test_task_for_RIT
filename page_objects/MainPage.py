from page_objects.Base import BasePage
from page_objects.RegistrationPage import RegistrationPage
from selenium.webdriver.common.by import By
from page_objects.AuthorizationPage import AuthorizationPage

class MainPage(BasePage):
    """Главная страница"""

    REGISTRATION_BUTTON = (By.XPATH, "//a[@href = '/bugs/signup_page.php']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/bugs/login_page.php?return=%2Fbugs%2Fmy_view_page.php']")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "a[href='/bugs/login_page.php?return=%2Fbugs%2Fmy_view_page.php']")

    def go_to_registration_form(self):
        self._click(*self.REGISTRATION_BUTTON)
        return RegistrationPage(self.driver)

    def go_to_authorization_form(self):
        self._click(*self.AUTHORIZATION_BUTTON)
        return AuthorizationPage(self.driver)
