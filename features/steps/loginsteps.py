from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# import logging as log

@given('I am in login page')
def login_page(context):
    #context.driver = webdriver.Chrome("C:\\Users\\takia\\Documents\\workspace\\selenium-python-automation\\chromedriver.exe")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)
    print('I am in login page')
    # assert 1 == 1
    # log.info('I am in login page')


@when('i enter username')
def valid_user(context):
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    context.driver.find_element_by_xpath(username).send_keys("Admin")
    print('I enter username')


@when('i enter password')
def valid_password(context):
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    context.driver.find_element_by_xpath(password).send_keys("admin123")
    print('i enter password')


@when('I click on submit button')
def submit_btn(context):
    submit_btn = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    context.driver.find_element_by_xpath(submit_btn).click()
    print('I click on submit button')


@then('i should see home page')
def home_page(context):
    print('i should see home page')
    assert context.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    context.driver.close()