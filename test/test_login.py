import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_successfully(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.driver.implicitly_wait(1000)
        username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.driver.find_element_by_xpath(username).send_keys("Admin")
        self.driver.find_element_by_xpath(password).send_keys("admin123")
        self.driver.find_element_by_xpath(login).click()
        print("\n tc1...........>success")

    #def test_user_can_click_info_page(self):
        myinfo_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
        firstname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
        lastname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
        self.driver.find_element_by_xpath(myinfo_btn).click()
        self.driver.find_element_by_xpath(firstname_path).send_keys("nihad")
        self.driver.find_element_by_xpath(lastname_path).send_keys("ferdousi")
        print("\n tc2...........>success")

    #def test_user_can_click_admin_page(self):
        admin_path = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
        System_Users_user_role_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div"
        System_Users_status_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div"
        admin_user_add_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
        add_user_role_dropdown_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
        admin_job_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
        admin_job_job_titles_path = "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[2] / ul / li[1] / a"
        admin_organization_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]"
        admin_organization_locations_path = "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[3] / ul / li[2]"
        admin_qualifications_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]"
        admin_qualifications_education_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]"
        admin_nationalities_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]"
        admin_more_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]"
        admin_corporate_branding_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[1]/li/a"
        admin_configuration_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/li/a"
        admin_configuration_email_configuration_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[1]/a"
        self.driver.find_element_by_xpath(admin_path).click()
        self.driver.find_element_by_xpath(System_Users_user_role_path).click()
        self.driver.find_element_by_xpath(System_Users_status_path).click()
        self.driver.find_element_by_xpath(admin_user_add_path).click()
        self.driver.find_element_by_xpath(add_user_role_dropdown_path).click()
        self.driver.find_element_by_xpath(admin_job_path).click()
        self.driver.find_element_by_xpath(admin_job_job_titles_path).click()
        self.driver.find_element_by_xpath(admin_organization_path).click()
        self.driver.find_element_by_xpath(admin_organization_locations_path).click()
        self.driver.find_element_by_xpath(admin_qualifications_path).click()
        self.driver.find_element_by_xpath(admin_qualifications_education_path).click()
        self.driver.find_element_by_xpath(admin_nationalities_path).click()
        self.driver.find_element_by_xpath(admin_more_path).click()
        self.driver.find_element_by_xpath(admin_corporate_branding_path).click()
        self.driver.find_element_by_xpath(admin_more_path).click()
        self.driver.find_element_by_xpath(admin_configuration_path).click()
        self.driver.find_element_by_xpath(admin_configuration_email_configuration_path).click()
        print("\n tc3...........>success")

    #def test_user_can_click_leave_page(self):
        leave_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a"
        leave_apply_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]"
        leave_my_leave_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
        more_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
        assign_leave_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a"
        leave_type_select_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div"
        self.driver.find_element_by_xpath(leave_btn).click()
        self.driver.find_element_by_xpath(leave_apply_path).click()
        self.driver.find_element_by_xpath(leave_my_leave_path).click()
        self.driver.find_element_by_xpath(more_path).click()
        self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/div/li/a").click()
        # driver.find_element_by_xpath(assign_leave_icon).click()
        self.driver.find_element_by_xpath(leave_type_select_path).click()
        print("\n tc4...........>success")

    #def test_user_can_click_performance_page(self):
        performance_icon = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span"
        my_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
        employee_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a"
        self.driver.find_element_by_xpath(performance_icon).click()
        self.driver.find_element_by_xpath(my_trackers_path).click()
        self.driver.find_element_by_xpath(employee_trackers_path).click()
        print(driver.current_url)
        self.driver.save_screenshot("image.png")
        print("\n tc5...........>success")
        self.driver.close()

    def test_logout_successfully(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.driver.implicitly_wait(1000)
        username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
        logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
        self.driver.find_element_by_xpath(username).send_keys("Admin")
        self.driver.find_element_by_xpath(password).send_keys("admin123")
        self.driver.find_element_by_xpath(login).click()
        self.driver.find_element_by_xpath(paul).click()
        self.driver.find_element_by_xpath(logout).click()
        print("\n tc6...........>success")
        self.driver.close()

    def test_user_should_not_login_with_invalid_credential(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.driver.implicitly_wait(1000)
        username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        invalid_message = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
        self.driver.find_element_by_xpath(username).send_keys("abc")
        self.driver.find_element_by_xpath(password).send_keys("admin12345")
        self.driver.find_element_by_xpath(login).click()
        error_message = self.driver.find_element_by_xpath(invalid_message).text
        assert "Invalid credentials" in error_message
        print("\n tc7...........>success")

        # def test_close_browser(self):
        self.driver.close()
