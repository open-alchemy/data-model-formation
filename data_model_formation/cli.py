"""Command line interface for DataModelFormation."""

import click


@click.command()
@click.argument("name")
def main():
    """CLI entry point."""
    print("hi")
