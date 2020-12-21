import random
import string
import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TeamsLocators:
    create_team_button = (By.XPATH, "//*[@id='create-team']")
    team_name_field = (By.XPATH, "//input[@data-testid='team-name']")
    create_submit_button = (By.XPATH, "//*[@id='create-team-submit']")


class TeamsMethods(BasePage):

    def create_team(self):
        time.sleep(1.5)
        create_team_click = self.find_element(TeamsLocators.create_team_button)
        create_team_click.click()
        time.sleep(2)
        team_name = self.find_element(TeamsLocators.team_name_field)
        team_name.click()
        randstring = 'test_auto_'.join(random.choices(string.digits, k=3))
        team_name.send_keys(randstring)
        submit = self.find_element(TeamsLocators.create_submit_button)
        submit.click()
        return create_team_click, team_name, submit