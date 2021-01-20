from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ReportsLocators:
    my_reports_but = (By.XPATH, "//div[@id='my']")
    shared_but = (By.XPATH, "//div[@id='shared']")
    create_rep_but = (By.XPATH, "//div[@id='createReport']")
    timeline_report_type_button = (By.XPATH,
                                   "//div[@data-report-type='timeline'")
    failed_alert_window = (By.XPATH,
                           "# //*[contains(text(),'You do not have a valid license for the app.')")

class Reportsmethods(BasePage):

    def access_create_report_page(self):
        create_report = self.find_element(ReportsLocators.create_rep_but)
        create_report.click()
        return create_report

    def access_my_reports_page(self):
        my_reports = self.find_element(ReportsLocators.my_reports_but)
        my_reports.click()
        return my_reports

    def create_timeline_report(self):
        timeline_rep = self.find_element(ReportsLocators.timeline_report_type_button)
        timeline_rep.click()
        return timeline_rep



