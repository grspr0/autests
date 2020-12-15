from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class LoginLocators:

    mail_form = (By.XPATH, "//input[@id='username']")
    subm_button = (By.CSS_SELECTOR, "#login-submit > span > span")
    password_form = (By.XPATH, "//input[@id='password']")
    login_but = (By.CSS_SELECTOR, "#login-submit > span > span")


class Login(BasePage):

    def login_process(self, login, password):
        login_form = self.find_element(LoginLocators.mail_form, time=2)
        login_form.click()
        login_form.send_keys(login)
        self.find_element(LoginLocators.subm_button, time=2).click()
        time.sleep(1)
        password_form = self.find_element(LoginLocators.password_form, time=2)
        password_form.click()
        password_form.send_keys(password)
        self.find_element(LoginLocators.login_but, time=2).click()
        return login, password











