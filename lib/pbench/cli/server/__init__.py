"""
Create a click context object that holds the state of the server
invocation. The CliContext will keep track of passed parameters,
what command created it, which resources need to be cleaned up,
and etc.

We create an empty object at the beginning and populate the object
with configuration, group names, at the beginning of the server
execution.
"""

import click


class CliContext:
    """Initialize an empty click object"""

    pass


pass_cli_context = click.make_pass_decorator(CliContext, ensure=True)
