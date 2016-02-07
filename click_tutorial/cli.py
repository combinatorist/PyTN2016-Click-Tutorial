import click

# Note: this name gives the name out to the CLI (including help?)
# Note: it's also great if you want to use a python keyword for your command
@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """

# Note: we control belonging to the group by using the group name
@cli.command()
def status():
    ""
    Output status info.
    ""
    click.echo("status: ok")

if __name__ == '__main__':
    cli()
