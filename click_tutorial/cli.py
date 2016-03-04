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

@cli.command()
def prompt2():
    click.confirm("Are you sure?", abort=True)
    click.echo("OK")

if __name__ == '__main__':
    cli()

