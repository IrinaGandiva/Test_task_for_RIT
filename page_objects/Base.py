from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, *locator):
        return self.driver.find_element(*locator)

    def _click(self, *locator):
        ActionChains(self.driver).move_to_element(self.__element(*locator)).click().perform()

    def _input(self, *locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, *locator, wait=5):
        element = self.driver.find_element(*locator)
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(element))

    def _get_element_text(self, *locator):
        return self.driver.find_element(*locator).text

    def _input_value_push_enter(self, *locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value + Keys.ENTER)
