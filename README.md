# Sceptre Test Rig

A simple acceptance testrig for Sceptre. The purpose of this testrig is to
demonstrate that all components can hang together to meet the needs of our
users.

This testrig isn't to test the integration between Providers and their
respective services, such as AWS Provider and CloudFormation. Those tests should
be contained within the individual Provider repositories.

Here we will test the full lifecycle of the application including:

- Can I take actions ("create/update/delete/list) on a Stack?
- Can I create a Provider and use it as intended?
- Can I launch multiple stacks using the appropriate providers?
- Does using sceptre through its API remain straightforward?
