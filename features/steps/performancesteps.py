import time

from behave import *


@when('i click performance button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span").click()
    time.sleep(2)
    print('i click performance button')


@when('i click my trackers btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
    time.sleep(2)
    print('i click my trackers btn')


@when('i click employee trackers btn')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click()
    time.sleep(2)
    print('i click employee trackers btn')


@then('i should see EmployeePerformanceTrackerList page')
def step_impl(context):
    assert context.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/performance/viewEmployeePerformanceTrackerList"
    time.sleep(2)
    print('i should see EmployeePerformanceTrackerList page')

