from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class LoginLocators:

    mail_form = (By.XPATH, "//input[@id='username']")
    subm_button = (By.XPATH, "//button[@id='login-submit']")
    password_form = (By.XPATH, "//input[@id='password']")
    login_but = (By.XPATH, "//button[@id='login-submit']")
    profile_icon = (By.XPATH,
                    "//span[@data-testid='atlassian-navigation--secondary-actions--profile--menu-trigger']")
    logout_button = (By.XPATH,
                     "//a[@data-testid='atlassian-navigation--secondary-actions--profile--menu-popup--footer--items--item-log-out']")
    logout_submit_button = (By.XPATH, "//*[@id='logout-submit']")

class LoginLogout(BasePage):


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

    def logout_process(self):
        profile = self.find_element(LoginLocators.profile_icon)
        profile.click()
        logout = self.find_element(LoginLocators.logout_button)
        logout.click()
        time.sleep(0.5)
        submit_logout = self.find_element(LoginLocators.logout_submit_button)
        submit_logout.click()
        return profile, logout, submit_logout











