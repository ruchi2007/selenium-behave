from behave import *


@when('i click myinfo button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click()
    print('i click myinfo button')


@when('i enter firstname')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys(
        "nihad")
    print('i enter firstname')


@when('i enter lastname')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys(
        "ferdousi")
    print('i enter lastname')


@then('i should see myinfo page')
def step_impl(context):
    print('i should see myinfo page')
    assert context.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
    context.driver.close()
