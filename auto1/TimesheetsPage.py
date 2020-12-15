from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time

# class TimesheetsLocators:
#
#     log_time_button = (By.XPATH, "//button[@id='addLog']")


class LogTimeLocators:

    reports_but = (By.XPATH, "//*[@data-testid='switcher-button-Reports']")
    timeline_button = (By.XPATH, "//*[@id='calendar']")
    log_time_button = (By.ID, "addLog")
    issue_selector_field = (By.XPATH, "//div[@data_testid='issue-selector-open-button']")
    search_field = (By.XPATH, "//input[@id='searchIssue']")
    option_field = (By.XPATH, "//li[@data-title='task_123']")
    time_spent_field = (By.XPATH, "//input[@data-testid='logged-time-field']")
    save_button = (By.XPATH, "//button[@data-testid='save-worklog-button']")


class LogTime(BasePage):

    def access_log_time(self):
        # timeline_view = self.find_element(LogTimeLocators.timeline_button)
        # timeline_view.click()
        rep_cl = self.find_element(LogTimeLocators.reports_but)
        rep_cl.click()
        log_time = self.find_element(LogTimeLocators.log_time_button)
        log_time.click()
        issue_selector = self.find_element(LogTimeLocators.issue_selector_field)
        issue_selector.click()
        search = self.find_element(LogTimeLocators.search_field)
        search.click()
        search.send_keys("test_123")
        option = self.find_element(LogTimeLocators.option_field)
        option.click()
        option.send_keys("2h")
        save = self.find_element(LogTimeLocators.save_button)
        save.click()
        # return search, option
