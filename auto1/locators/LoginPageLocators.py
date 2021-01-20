from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class LoginLocators:

    login_form = (By.CSS_SELECTOR, "#username")
    continue_button = (By.CSS_SELECTOR, "#login-submit")
    password_form = (By.CSS_SELECTOR,
                     "#password")
    login_but = (By.CSS_SELECTOR, "#login-submit")
    profile_icon = (By.CSS_SELECTOR,
                    "#jira-frontend > div.sc-brqgnP.jbCidx > div > div.sc-jWBwVP.klvkUU > div > header > div > span:nth-child(5) > div > button > span > span > div")
    logout_button = (By.CSS_SELECTOR,
                    "#jira > div.atlaskit-portal-container > div:nth-child(4) > div > span > div > div > div.css-usnzv1 > span > a > div > span > span")
    logout_submit_button = (By.CSS_SELECTOR, "#logout-submit")


class LoginLogout(BasePage):

    def login_process(self, login, password):
        login_form = self.find_element(LoginLocators.login_form)
        login_form.click()
        login_form.send_keys(login)
        self.find_element(LoginLocators.continue_button).click()
        time.sleep(0.2)
        password_form = self.find_element(LoginLocators.password_form)
        password_form.click()
        password_form.send_keys(password)
        self.find_element(LoginLocators.login_but).click()
        return login, password

    def logout_process(self):
        profile = self.find_element(LoginLocators.profile_icon)
        profile.click()
        logout = self.find_element(LoginLocators.logout_button)
        logout.click()
        time.sleep(0.5)
        submit_logout = self.find_element(LoginLocators.logout_submit_button)
        submit_logout.click()
        return profile, logout, submit_logout











