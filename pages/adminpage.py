class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
        self.System_Users_user_role_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div"
        self.System_Users_status_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div"
        self.add_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
        self.admin_user_role_dropdown_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
        self.admin_job_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
        self.admin_job_job_titles_path = "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[2] / ul / li[1] / a"
        self.admin_organization_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]"
        self.admin_organization_locations_btn = "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[3] / ul / li[2]"
        self.admin_qualifications_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]"
        self.admin_qualifications_education_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]"
        self.admin_nationalities_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]"
        self.admin_more_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]"
        self.admin_corporate_branding_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[1]/li/a"
        self.admin_more_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]"
        self.admin_configuration_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/li/a"
        self.admin_configuration_email_configuration_btn = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[1]/a"

    def click_admin_btn(self):
        self.driver.find_element_by_xpath(self.admin_btn).click()
        self.driver.find_element_by_xpath(self.System_Users_user_role_icon).click()
        self.driver.find_element_by_xpath(self.System_Users_status_icon).click()
        self.driver.find_element_by_xpath(self.add_btn).click()
        self.driver.find_element_by_xpath(self.admin_user_role_dropdown_icon).click()
        self.driver.find_element_by_xpath(self.admin_job_path).click()
        self.driver.find_element_by_xpath(self.admin_job_job_titles_path).click()
        self.driver.find_element_by_xpath(self.admin_organization_path).click()
        self.driver.find_element_by_xpath(self.admin_organization_locations_btn).click()
        self.driver.find_element_by_xpath(self.admin_qualifications_btn).click()
        self.driver.find_element_by_xpath(self.admin_qualifications_education_btn).click()
        self.driver.find_element_by_xpath(self.admin_nationalities_btn).click()
        self.driver.find_element_by_xpath(self.admin_more_btn).click()
        self.driver.find_element_by_xpath(self.admin_corporate_branding_btn).click()
        self.driver.find_element_by_xpath(self.admin_more_btn).click()
        self.driver.find_element_by_xpath(self.admin_configuration_btn).click()
        self.driver.find_element_by_xpath(self.admin_configuration_email_configuration_btn).click()
