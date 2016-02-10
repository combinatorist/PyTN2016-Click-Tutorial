import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """
#    click.echo("Hello, PyTN!")

@cli.command() 
def status():
  # NOTE: we don't need '\n' since click includes that by default.
  click.echo("status: ok")

if __name__ == '__main__':
    cli()
