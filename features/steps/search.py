from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I Navigate to Home Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


@when(u'I enter valid product name in search field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id = 'search']//button").click()


@then(u'Valid product displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.close()


@when(u'I enter invalid product name in search field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
        expected_text)
    context.driver.close()


@when(u'I dont enter anything in search field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
