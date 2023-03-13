import click
from substring import get_max_substring


@click.command()
@click.option("--string", prompt="The string", help="The input sring")
def substring(string):
    result = get_max_substring(string)
    click.echo(f"The length of the longest substring is {result}!")


if __name__ == "__main__":
    substring()
