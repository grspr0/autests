from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time

class jira_locators:

    mail_form = (By.XPATH, "//input[@id='username']")
    subm_button = (By.CSS_SELECTOR, "#login-submit > span > span")
    password_form = (By.XPATH, "//input[@id='password']")
    login_but = (By.CSS_SELECTOR, "#login-submit > span > span")
    apps_but = (By.XPATH, "//span[contains(text(),'Apps')]")
    timesh = (By.XPATH, "//span[contains(text(),'My Timesheets')]")


class Login(BasePage):

    def login_process(self, login, password):
        login_form = self.find_element(jira_locators.mail_form, time=2)
        login_form.click()
        login_form.send_keys(login)
        self.find_element(jira_locators.subm_button, time=2).click()
        time.sleep(1)
        password_form = self.find_element(jira_locators.password_form, time=2)
        password_form.click()
        password_form.send_keys(password)
        self.find_element(jira_locators.login_but, time=2).click()
        return login, password

    def access_RB(self):
        apps = self.find_element(jira_locators.apps_but)
        apps.click()
        timesheets = self.find_element(jira_locators.timesh)
        timesheets.click()
    # def click_on_search(self):
    #     return self.find_element(google_locators.search_button, time=2).click()










