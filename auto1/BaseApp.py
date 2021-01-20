from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://id.atlassian.com/login?continue=https%3A%2F%2Fqwert657.atlassian.net%2Flogin%3FredirectCount%3D1%26application%3Djira&application=jira"

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find elements by locator {locator}")

    def switch_to(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_frame(self):
        # time.sleep(7.5)
        return self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

    def go_out_frame(self):
        # time.sleep(3.5)
        return self.driver.switch_to.default_content()

