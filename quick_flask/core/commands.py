# Description: This file contains the CLI commands for the quick_flask package.
import click
from .createfile import createfile

@click.group()
def main():
    pass

@main.command()
@click.option('--name', help='Name of the person to greet.', required=True, prompt="What is your name?")
@click.argument('number')
def name(name, number):
    for _ in range(int(number)):
        click.echo(f"Hello {name}!")

@main.command()
@click.option('--hello', help='Hello things')
def hello(hello):
    click.echo(f"Hello World! {hello}") 

@main.command()
def goodbye():
    click.echo(f"Goodbye World!")

main.add_command(createfile)
    
