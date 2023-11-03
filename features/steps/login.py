from behave import *


@given(u'I navigate to Login Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigate to Login Page')


@when(u'I enter valid email and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and password')


@when(u'I click on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on login button')


@then(u'I should get logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get logged in')


@when(u'I enter valid email and invalid password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and invalid password')


@then(u'I should get proper warning')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get proper warning')


@when(u'I enter invalid email and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid email and password')