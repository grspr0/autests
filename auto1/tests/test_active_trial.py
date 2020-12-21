from locators.LoginPageLocators import LoginLogout
from locators.JiraAppsPageLocators import Apps
from locators.TimesheetsPageLocators import MyTimesheetsTimeline
from locators.ManageAppsPageLocators import ManageYourApps
from locators.ReportsMainPageLocators import Reportsmethods
from locators.TimelineReportPageLocators import TimelineRepsMethods
from locators.Report_Builder_locators import RB
from locators.TeamsMainLocators import TeamsMethods


def test_activetrial(browser):
    jira_login = LoginLogout(browser)
    ReportBuilder = RB(browser)
    jira_login.go_to_site()
    jira_login.login_process("kononovi467@gmail.com", "Solo1996")
    jira_apps = Apps(browser)
    jira_apps.access_apps()
    jira_apps.access_manage_your_apps()
    manage = ManageYourApps(browser)
    manage.apps_rb_access()
    manage.license_status_dropdown_access()
    manage.active_trial_status()
    jira_apps.access_apps()
    jira_apps.access_Timesheets()
    rb_logtime = MyTimesheetsTimeline(browser)
    rb_logtime.go_to_frame()
    rb_logtime.access_timeline_view()
    rb_logtime.access_log_time()
    rb_logtime.log_time("task_123", "6h")
    ReportBuilder.access_reports_from_RB_main()
    new_rep = Reportsmethods(browser)
    new_rep.go_to_frame()
    new_rep.access_create_report_page()
    new_rep.create_timeline_report()
    new_rep.go_to_frame()
    new_timeline_rep = TimelineRepsMethods(browser)
    new_timeline_rep.create_timeline_report("test_name_6")
    ReportBuilder.access_teams()
    new_team = TeamsMethods(browser)
    new_team.go_to_frame()
    new_team.create_team()
    new_timeline_rep.go_out_frame()
    jira_login.logout_process()
#
#
# def test_trial(browser):
#     jira_login = LoginLogout(browser)
#     jira_login.go_to_site()
#     jira_login.login_process("kononovi467@gmail.com", "Solo1996")
#     jira_apps = Apps(browser)
#     jira_apps.access_apps()
#     jira_apps.access_manage_your_apps()
#     manage = ManageYourApps(browser)
#     manage.apps_rb_access()
#     manage.license_status_dropdown_access()
#     manage.inactive_trial_status()
#     jira_apps.access_apps()
#     jira_apps.access_Reports()
#     jira_apps.go_to_frame()
#     new_rep = Reportsmethods(browser)
#     new_rep.access_create_report_page()
#     new_rep.create_timeline_report()
#     new_rep.go_to_frame()
#     new_rep.failed_alert()
#     new_rep.go_out_frame()
#     jira_apps.access_apps()
#     jira_apps.access_manage_your_apps()
#     manage = ManageYourApps(browser)
#     manage.apps_rb_access()
#     manage.license_status_dropdown_access()
#     manage.active_trial_status()
#     jira_login.logout_process()







