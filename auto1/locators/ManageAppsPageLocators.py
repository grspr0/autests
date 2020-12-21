from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class ManageYourAppsLotacors:
    report_builder = (By.XPATH, "//h4[contains(text(),'Report Builder: Timesheets and Data Analysis')]")
    access_token_status = (By.XPATH, "//select[@class='select medium-field token-state']")
    unlicensed = (By.XPATH, "//option[@value='NONE']")
    active_trial = (By.XPATH, "//option[@value='ACTIVE_TRIAL']")
    inactive_trial = (By.XPATH, "//option[@value='INACTIVE_TRIAL']")
    active_subscription = (By.XPATH, "//option[@value='ACTIVE_SUBSCRIPTION']")
    cancelled_subscription = (By.XPATH, "//option[@value='ACTIVE_SUBSCRIPTION_CANCELLED']")
    inactive_subscription = (By.XPATH, "//option[@value='INACTIVE_SUBSCRIPTION']")


class ManageYourApps(BasePage):

    def apps_rb_access(self):
        report_builder_app = self.find_element(ManageYourAppsLotacors.report_builder)
        report_builder_app.click()
        time.sleep(0.5)
        return report_builder_app

    def license_status_dropdown_access(self):
        access_token_dropdown = self.find_element(ManageYourAppsLotacors.access_token_status)
        access_token_dropdown.click()
        time.sleep(0.5)
        return access_token_dropdown

    def unlicensed_token_status(self):
        unlicensed_option = self.find_element(ManageYourAppsLotacors.unlicensed)
        unlicensed_option.click()
        time.sleep(0.5)
        return unlicensed_option

    def active_trial_status(self):
        active_option = self.find_element(ManageYourAppsLotacors.active_trial)
        active_option.click()
        time.sleep(0.5)
        return active_option

    def inactive_trial_status(self):
        inactive_trial_opt = self.find_element(ManageYourAppsLotacors.inactive_trial)
        inactive_trial_opt.click()
        time.sleep(0.5)
        return inactive_trial_opt

    def active_subscription_status(self):
        active_subscr_opt = self.find_element(ManageYourAppsLotacors.active_subscription)
        active_subscr_opt.click()
        time.sleep(0.5)
        return active_subscr_opt

    def cancelled_subscription_status(self):
        cancelled_subscr_opt = self.find_element(ManageYourAppsLotacors.cancelled_subscription)
        cancelled_subscr_opt.click()
        time.sleep(0.5)
        return cancelled_subscr_opt

    def inactive_subscription_status(self):
        inactive_subscr_opt = self.find_element(ManageYourAppsLotacors.inactive_subscription)
        inactive_subscr_opt.click()
        time.sleep(0.5)
        return inactive_subscr_opt
