from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('i am in home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    print('i am in home page')


@when('i click admin button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()


@when('i click System_Users_user_role_icon')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click()


@when('i click System_Users_status_icon')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div").click()


@when('I click add btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()


@then('i should see add user page')
def step_impl(context):
    assert context.driver.current_url == (
        "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")


@when('i click jobs btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()


@when('I click job titles btn')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[2] / ul / li[1] / a").click()


@then('i should see job titles page')
def step_impl(context):
    assert context.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList"


@when('i click organization btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click()


@when('i click organization_locations btn')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "// *[ @ id = 'app'] / div[1] / div[1] / header / div[2] / nav / ul / li[3] / ul / li[2]").click()


@then('i should see organization_locations page')
def step_impl(context):
    assert context.driver.current_url == ("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")


@when('i click qualifications btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]").click()


@when('i click qualifications_education btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]").click()


@then('i should see qualifications_education page')
def step_impl(context):
    assert context.driver.current_url == ("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewEducation")


@when('i click nationalities')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]").click()


@then('i should see nationalities page')
def step_impl(context):
    assert context.driver.current_url == ("https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")
