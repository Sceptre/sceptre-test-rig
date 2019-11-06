from pytest_bdd import scenario, given, when, then


@scenario('features/stack.feature', 'Create a Stack')
def test_create():
    pass


@given("A provider exists")
def provider(provider):
    provider


@given("a create_command exists")
def create_command(create_command):
    create_command


@when("I try to create a stack")
def create_a_stack():
    pass


@then("The output is \"create stack completed\"")
def output_is_create_complete():
    pass
