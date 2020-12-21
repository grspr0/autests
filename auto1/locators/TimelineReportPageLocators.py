from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class TimelineRepsLocators:
    new_report_field = (By.XPATH, "//input[@placeholder='New Report']")
    save_but = (By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div[4]/div[1]/span/button")
    success_alert_window = (By.XPATH, "//*[contains(text(),'Report was created')]")
    export_dropdown= (By.XPATH,
                      "//*[@id='root']/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button/span")
    csv_opt = (By.XPATH, "//*[@id='csv']")
    pdf_opt = (By.XPATH, "//*[@id='pdf']")
    report_create_success = (By.XPATH, "//*[contains(text(),'Report was created')]")


class TimelineRepsMethods(BasePage):

    def create_timeline_report(self, repname):
        new_report_name = self.find_element(TimelineRepsLocators.new_report_field)
        new_report_name.click()
        new_report_name.send_keys(repname)
        save_but_click = self.find_element(TimelineRepsLocators.save_but)
        save_but_click.click()
        return new_report_name, save_but_click

    def export(self):
        open_dropdown = self.find_element(TimelineRepsLocators.export_dropdown)
        open_dropdown.click()
        return  open_dropdown

    def csv_opt(self):
        csv_option = self.find_element(TimelineRepsLocators.csv_opt)
        csv_option.click()

    def pdf_opt(self):
        pdf_option = self.find_element(TimelineRepsLocators.pdf_opt)
        pdf_option.click()

    def report_created_alert(self):
        try:
            alert = self.find_element(TimelineRepsLocators.report_create_success)
            assert alert.text == 'Report was created'
        except Exception:
            print("You have no permission")

