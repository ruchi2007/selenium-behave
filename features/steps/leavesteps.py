from behave import *


@when('i click leave button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
    print('i click leave button')


@when('i click leave apply btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
    print('i click leave apply btn')


@when('i click leave my leave btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()
    print('i click leave my leave btn')


@then('i should see my leave list page')
def step_impl(context):
    assert context.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList"
    print('i should see my leave list page')
