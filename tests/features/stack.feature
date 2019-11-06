Feature: Stack
    Can act upon Stacks

Scenario: Create a Stack
    Given: A provider exists
    And: a create_command exists
    When: I try to create a stack
    Then: The output is "create stack completed"
