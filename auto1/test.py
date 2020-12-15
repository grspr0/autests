from Loginpage import Login
from JiraAppspage import Apps
from TimesheetsPage import LogTime
from ManageAppsPage import ManageYourApps
import time


def test_access(browser):
    jira_login = Login(browser)
    jira_login.go_to_site()
    jira_login.login_process("kononovi467@gmail.com", "Solo1996")
    jira_apps = Apps(browser)
    jira_apps.access_manage_your_apps()
    manage = ManageYourApps(browser)
    manage.active_trial_status()
    jira_apps.access_Timesheets()
    rb_logtime = LogTime(browser)
    time.sleep(5)
    rb_logtime.access_log_time()
    time.sleep(4)



    # rb_logtime = LogTime(browser)
    # rb_logtime.access_log_time()



