import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_setup():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)


def test_login_successfully():
# login_page
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    driver.find_element_by_xpath(username).send_keys("Admin")
    driver.find_element_by_xpath(password).send_keys("admin123")
    driver.find_element_by_xpath(login).click()

#info_page
    myinfo_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
    firstname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
    lastname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
    driver.find_element_by_xpath(myinfo_btn).click()
    driver.find_element_by_xpath(firstname_path).send_keys("nihad")
    driver.find_element_by_xpath(lastname_path).send_keys("ferdousi")


#admin_page
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
    driver.find_element_by_xpath(admin_path).click()
    driver.find_element_by_xpath(System_Users_user_role_path).click()
    driver.find_element_by_xpath(System_Users_status_path).click()
    driver.find_element_by_xpath(admin_user_add_path).click()
    driver.find_element_by_xpath(add_user_role_dropdown_path).click()
    driver.find_element_by_xpath(admin_job_path).click()
    driver.find_element_by_xpath(admin_job_job_titles_path).click()
    driver.find_element_by_xpath(admin_organization_path).click()
    driver.find_element_by_xpath(admin_organization_locations_path).click()
    driver.find_element_by_xpath(admin_qualifications_path).click()
    driver.find_element_by_xpath(admin_qualifications_education_path).click()
    driver.find_element_by_xpath(admin_nationalities_path).click()
    driver.find_element_by_xpath(admin_more_path).click()
    driver.find_element_by_xpath(admin_corporate_branding_path).click()
    driver.find_element_by_xpath(admin_more_path).click()
    driver.find_element_by_xpath(admin_configuration_path).click()
    driver.find_element_by_xpath(admin_configuration_email_configuration_path).click()


#leave_page
    leave_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a"
    leave_apply_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]"
    leave_my_leave_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
    more_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
    assign_leave_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a"
    leave_type_select_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div"
    driver.find_element_by_xpath(leave_btn).click()
    driver.find_element_by_xpath(leave_apply_path).click()
    driver.find_element_by_xpath(leave_my_leave_path).click()
    driver.find_element_by_xpath(more_path).click()
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/div/li/a").click()
    # driver.find_element_by_xpath(assign_leave_icon).click()
    driver.find_element_by_xpath(leave_type_select_path).click()

#performance_page
    performance_icon = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span"
    my_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
    employee_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a"
    driver.find_element_by_xpath(performance_icon).click()
    driver.find_element_by_xpath(my_trackers_path).click()
    driver.find_element_by_xpath(employee_trackers_path).click()
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/performance/viewEmployeePerformanceTrackerList"
    actual_url = driver.current_url
    assert expected_url == actual_url
    print(driver.current_url)
    driver.save_screenshot("image.png")
    title = driver.title
    assert title == "OrangeHRM"


def test_logout_successfully():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
    driver.find_element_by_xpath(username).send_keys("Admin")
    driver.find_element_by_xpath(password).send_keys("admin123")
    driver.find_element_by_xpath(login).click()
    driver.find_element_by_xpath(paul).click()
    driver.find_element_by_xpath(logout).click()


def test_user_should_not_login_with_invalid_credential():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    invalid_message = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
    driver.find_element_by_xpath(username).send_keys("abc")
    driver.find_element_by_xpath(password).send_keys("admin12345")
    driver.find_element_by_xpath(login).click()
    error_message = driver.find_element_by_xpath(invalid_message).text
    assert "Invalid credentials" in error_message


#def test_closebrowser():
    driver.close()
    driver.quit()
