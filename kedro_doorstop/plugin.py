"""Kedro plugin for integrating doorstop into the Kedro CLI."""

import click

DOORSTOP_VERSION = "2.1.1"


@click.group(name="Doorstop")
def commands():
    """Kedro plugin for integrating doorstep into the Kedro CLI."""
    pass


@commands.group(name="doorstop")
def doorstop_commands():
    """Manage software requirements with Doorstop."""
    pass


@doorstop_commands.command(name="info")
def info():
    """Command to output doorstop version in use."""
    print(f"doorstop version in use: {DOORSTOP_VERSION}")
