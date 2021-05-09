"""Command line interface for DataModelFormation."""

import io
import typing

import click

_FORMATS = typing.Literal["SQLALCHEMY", "DATACLASSES", "PYNAMODB"]


@click.command()
@click.argument("path", type=click.File("rt"))
@click.argument(
    "format_",
    type=click.Choice(typing.get_args(_FORMATS), case_sensitive=False),
)
def main(path: io.TextIOWrapper, format_: _FORMATS):
    """CLI entry point."""
    print(path.read())
    print(format_)
    print("hi")
