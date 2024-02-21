import click

@click.command()
@click.option('--name', help='Name of the file to create.', required=True, prompt="What is the name of the file?")
@click.argument('name')
@click.option('--extension', help='Extension of the file to create.', required=True, prompt="What the extension of the file?")
@click.argument('extension')
def createfile(name, extension):
    click.echo(f"Creating file...")
    with open(f"{name}.{extension}", "w") as f:
        f.write("Hello World!")
    click.echo(f"{name}file created!")
