from BaseApp import BasePage
from selenium.webdriver.common.by import By


class JiraAppsLocators:

    apps_but = (By.XPATH, "//span[contains(text(),'Apps')]")
    timesheets_but = (By.XPATH, "//a[@data-testid='atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-0']")
    reports_but = (By.XPATH, "//a[@data-testid='atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-1']")
    teams_but = (By.XPATH, "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--content--items--item-2']")
    find_new_but = (By.XPATH, "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-find-new-apps']")
    manage_your_apps_but = (By.XPATH, "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-manage-apps']")
    view_app_request_but = (By.XPATH, "//a[@data-testid = 'atlassian-navigation--primary-actions--addons--menu-popup--footer--items--item-app-requests']")


class Apps(BasePage):

    def access_Timesheets(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        timesheets = self.find_element(JiraAppsLocators.timesheets_but)
        timesheets.click()

    def access_Reports(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        reports = self.find_element(JiraAppsLocators.reports_but)
        reports.clock()

    def access_Teams(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        teams = self.find_element(JiraAppsLocators.teams_but)
        teams.click()

    def access_find_new_Apps(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        find_new_apps = self.find_element(JiraAppsLocators.find_new_but)
        find_new_apps.click()

    def access_manage_your_apps(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        manage_your_apps = self.find_element(JiraAppsLocators.manage_your_apps_but)
        manage_your_apps.click()

    def access_view_app_request(self):
        apps = self.find_element(JiraAppsLocators.apps_but)
        apps.click()
        view_app_request = self.find_element(JiraAppsLocators.view_app_request_but)
        view_app_request.click()


