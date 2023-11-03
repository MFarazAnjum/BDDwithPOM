from behave import *

@given(u'I navigate to Register Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigate to Register Page')


@when(u'I enter mandatory Fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter mandatory Fields')


@when(u'I click on continue button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on continue button')


@then(u'Account should get created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Account should get created')


@when(u'I enter all Fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter all Fields')


@when(u'I enter all Fields except email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter all Fields except email field')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter existing accounts email into email field')


@then(u'Proper warning message should be displayed for duplicate emails')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message should be displayed for duplicate emails')


@when(u'I dont enter anything into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I dont enter anything into the fields')


@then(u'Proper warning message should be displayed for mandatory field should be entered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message should be displayed for mandatory field should be entered')
