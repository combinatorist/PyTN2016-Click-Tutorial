import click

@click.command(name='pytn')
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
def cli(infile, outfile):
    """
    Output a greeting to PyTennessee!
    """
    text = infile.read()
    # test_02 checked that the CLI output didn't contain text
    # It was supposed to return the char count (as below)
    click.echo("Input File: " + str(len(text)), err=True)
    # The test didn't check for the color formatting
    click.secho(text, file=outfile)

if __name__ == '__main__':
    cli()
