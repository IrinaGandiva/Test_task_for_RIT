from page_objects.Base import BasePage
from page_objects.RegistrationPage import RegistrationPage
from selenium.webdriver.common.by import By
from page_objects.AuthorizationPage import AuthorizationPage
from page_objects.TaskCreationPage import TaskCreationPage


class MainPage(BasePage):
    """Главная страница"""

    REGISTRATION_BUTTON = (By.XPATH, "//a[@href = '/bugs/signup_page.php']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/bugs/login_page.php?return=%2Fbugs%2Fmy_view_page.php']")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "a[href='/bugs/login_page.php?return=%2Fbugs%2Fmy_view_page.php']")
    NEW_TASK_CREATION_BUTTON = (By.CSS_SELECTOR, "a[href='bug_report_page.php']")
    ALL_PROJECTS_BUTTON = (By.XPATH, "//a[@class='dropdown-toggle']")
    CHOOSE_MANTISBT_PROJECT = (By.XPATH, "//*[text()='mantisbt']")
    LOGO = (By.XPATH, "//*[@class='navbar-header']")
    SEARCH_FIELD = (By.XPATH, "//*[@name='bug_id']")

    def go_to_registration_form(self):
        self._click(*self.REGISTRATION_BUTTON)
        return RegistrationPage(self.driver)

    def go_to_authorization_form(self):
        self._click(*self.AUTHORIZATION_BUTTON)
        return AuthorizationPage(self.driver)

    def go_to_task_creation_page(self):
        self._click(*self.NEW_TASK_CREATION_BUTTON)
        return TaskCreationPage(self.driver)

    def click_all_projects_button(self):
        self._click(*self.ALL_PROJECTS_BUTTON)
        return self

    def choose_mantisbt_project_from_drop_down_list(self):
        self._click(*self.CHOOSE_MANTISBT_PROJECT)
        return self

    def click_logo(self):
        self._click(*self.LOGO)
        return self

    def enter_text_into_search_field(self, text):
        self._input_value_push_enter(*self.SEARCH_FIELD, value=text)
        return self
