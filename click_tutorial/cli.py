import click

@click.command(name='pytn')
@click.argument('names', nargs=-1)
def cli(names):
    """
    Output a greeting to PyTennessee!
    """
    for name in names:
      click.echo("name: {0}".format(name))

if __name__ == '__main__':
    cli()
