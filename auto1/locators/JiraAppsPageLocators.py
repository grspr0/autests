from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class JiraAppsLocators:

    apps_but = (By.XPATH, "//span[contains(text(),'Apps')]")
    timesheets_but = (By.XPATH,
                      "//a[@data-testid='atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-0']")
    reports_but = (By.XPATH,
                   "//a[@data-testid='atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-1']")
    teams_but = (By.XPATH,
                 "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-2']")
    find_new_but = (By.XPATH,
                    "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-find-new-apps']")
    manage_your_apps_but = (By.XPATH,
                            "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-manage-apps']")
    view_app_request_but = (By.XPATH,
                            "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-app-requests']")
    iframe_timesheets = (By.XPATH,
                         "//iframe[@id='proficient.developer.plugins.jira.worklog-pivot__worklogs-page__c896d8e']")


class Apps(BasePage):

    def access_apps(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        return apps

    def access_Timesheets(self):
        timesheets = self.find_element(JiraAppsLocators.timesheets_but)
        timesheets.click()
        time.sleep(0.5)
        return timesheets

    def access_Reports(self):
        reports = self.find_element(JiraAppsLocators.reports_but)
        reports.click()
        return reports

    def access_Teams(self):
        teams = self.find_element(JiraAppsLocators.teams_but)
        teams.click()
        return teams

    def access_find_new_Apps(self):
        find_new_apps = self.find_element(JiraAppsLocators.find_new_but)
        find_new_apps.click()
        return find_new_apps

    def access_manage_your_apps(self):
        manage_your_apps = self.find_element(JiraAppsLocators.manage_your_apps_but)
        manage_your_apps.click()
        return manage_your_apps

    def access_view_app_request(self):
        view_app_request = self.find_element(JiraAppsLocators.view_app_request_but)
        view_app_request.click()
        return view_app_request

