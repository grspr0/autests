from BaseApp import BasePage
from selenium.webdriver.common.by import By


class RbLocators:
    reports_but = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/div[2]/button/span")
    teams_but = (By.XPATH, "//button[@data-testid='switcher-button-Teams']")
    report_create_success = (By.XPATH, "//*[contains(text(),'Report was created')]")
    worlog_create_success = (By.XPATH, "//*[contains(text(),'Worklog was created')]")


class RB(BasePage):

    def access_reports_from_RB_main(self):
        reports = self.find_element(RbLocators.reports_but)
        reports.click()
        return reports

    def access_teams(self):
        teams = self.find_element(RbLocators.teams_but)
        teams.click()
        return teams
