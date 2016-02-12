import click

@click.command(name='pytn')
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
def cli(infile, outfile):
    """
    Output a greeting to PyTennessee!
    """
    text = infile.read()
    click.echo("Input File: " + str(len(text)), err=True)
    click.secho(text, file=outfile)

if __name__ == '__main__':
    cli()
