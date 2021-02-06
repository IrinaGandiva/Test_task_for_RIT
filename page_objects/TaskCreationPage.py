from page_objects.Base import BasePage
from selenium.webdriver.common.by import By


class TaskCreationPage(BasePage):
    """Страница создания задачи"""

    CATEGORY_DROP_DOWN_LIST = (By.XPATH, "//*[@id = 'category_id']")
    SUMMARY_FIELD = (By.XPATH, "//input[@id='summary']")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@id='description']")
    TASK_CREATION_BUTTON = (By.XPATH, "//input[@type = 'submit']")
    BUG_ID_FIELD = (By.XPATH, "//td[@class='bug-id']")
    TITLE_VIEW_TASK = (By.XPATH, "//h4[@class='widget-title lighter']")

    def choose_category(self, text):
        self._input_value_push_enter(*self.CATEGORY_DROP_DOWN_LIST, value=text)
        return self

    def input_summary_into_task_creation_form(self, text):
        self._input(*self.SUMMARY_FIELD, value=text)
        return self

    def input_description_into_task_creation_form(self, text):
        self._input(*self.DESCRIPTION_FIELD, value=text)
        return self

    def click_task_creation_button(self):
        self._click(*self.TASK_CREATION_BUTTON)
        return self

    def get_number_of_created_task(self):
        return self._get_element_text(*self.BUG_ID_FIELD)

    def waiting_for_title(self):
        self._wait_for_visible(*self.TITLE_VIEW_TASK)
        return self
