from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class TimeSheetsLocators:

    timeline_button = (By.XPATH, "//*[@id='timesheet']")
    log_time_button = (By.ID, "addLog")
    issue_selector_field = (By.XPATH, "//*[@data-testid='issue-selector-open-button']")
    search_field = (By.XPATH, "//input[@id='searchIssue']")
    option_field = (By.XPATH, "//li[@data-title='task_123']")
    time_spent_field = (By.XPATH, "//input[@data-testid='logged-time-field']")
    save_button = (By.XPATH, "//button[@data-testid='save-worklog-button']")
    iframe_xpath = (By.XPATH,
                    "//iframe[contains(@id, 'proficient.developer.plugins.jira.worklog-pivot__worklogs-page__2ce4f11c')]")
    worlog_create_success = (By.XPATH, "//*[contains(text(),'Worklog was created')]")

class MyTimesheetsTimeline(BasePage):

    def access_timeline_view(self):
        timeline = self.find_element(TimeSheetsLocators.timeline_button)
        timeline.click()
        return timeline

    def access_log_time(self):
        log_time = self.find_element(TimeSheetsLocators.log_time_button)
        log_time.click()
        return log_time

    def log_time(self, issue, timesp):
        issue_selector = self.find_element(TimeSheetsLocators.issue_selector_field)
        issue_selector.click()
        search = self.find_element(TimeSheetsLocators.search_field)
        search.click()
        search.send_keys(issue)
        time.sleep(2)
        option = self.find_element(TimeSheetsLocators.option_field)
        option.click()
        time_logged = self.find_element(TimeSheetsLocators.time_spent_field)
        time_logged.click()
        time_logged.send_keys(timesp)
        save = self.find_element(TimeSheetsLocators.save_button)
        save.click()
        return issue_selector, search, option, save

    def worklog_created_alert(self):
        try:
            alert = self.find_element(TimeSheetsLocators.worlog_create_success)
            assert alert.text == 'Worklog was created'
        except Exception:
            print("You have no permission")




