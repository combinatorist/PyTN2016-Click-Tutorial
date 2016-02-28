import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """

@cli.command(name="prompt1")
def prompter1():
    data = click.prompt("Data")
    click.echo('data: ' + data)

if __name__ == '__main__':
    cli()
