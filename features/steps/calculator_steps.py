from behave import given, when, then
from app.calculator import Calculator

calc = Calculator()


@given('I have numbers {a:d} and {b:d}')
def step_given(context, a, b):
    context.a = a
    context.b = b


@when('I add them')
def step_when(context):
    context.result = calc.add(context.a, context.b)


@then('the result should be {expected:d}')
def step_then(context, expected):
    assert context.result == expected
