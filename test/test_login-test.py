import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.adminpage import AdminPage
from pages.homepage import HomePage
from pages.infopage import InfoPage
from pages.leavepage import LeavePage
from pages.loginpage import LoginPage
from pages.performancepage import PerformancePage
from utils import usercredential

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_successfully(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(usercredential.username)
        lp.enter_password(usercredential.password)
        lp.click_submit_btn()
        print("\n tc1...........>success")

    def test_user_can_click_info_page(self):
        driver = self.driver
        ip = InfoPage(driver)
        ip.click_myinfo_btn()
        ip.enter_firstname("nihad")
        ip.enter_lastname("ferdousi")
        print("\n tc2...........>success")

    def test_user_can_click_admin_page(self):
        driver = self.driver
        ap = AdminPage(driver)
        ap.click_admin_btn()
        print("\n tc3...........>success")

    def test_user_can_click_leave_page(self):
        driver = self.driver
        lep = LeavePage(driver)
        lep.click_leave_btn()
        print("\n tc4...........>success")

    def test_user_can_click_performance_page(self):
        driver = self.driver
        pp = PerformancePage(driver)
        pp.click_performance_btn()
        print("\n tc5...........>success")

    def test_logout_successfully(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.click_logout_icon()
        print("\n tc6...........>success")

    def test_user_should_not_login_with_invalid_credential(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(usercredential.inv_username)
        lp.enter_password(usercredential.inv_password)
        lp.click_submit_btn()
        assert "Invalid credentials" in lp.error_text_message()
        print("\n tc7...........>success")
