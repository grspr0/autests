from Jirapages import Login
import time


def test_login(browser):
    jira_main = Login(browser)
    jira_main.go_to_site()
    jira_main.login_process("kononovi467@gmail.com", "Solo1996")



def test_access(browser):
    jira_main = Login(browser)
    jira_main.go_to_site()
    jira_main.login_process("kononovi467@gmail.com", "Solo1996")
    jira_main.access_RB()
    time.sleep(2)


