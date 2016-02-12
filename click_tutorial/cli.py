import click

@click.group(name='pytn')
@click.option('--input-string1', help='Optional input string.')
@click.option('--input-string2', metavar='<string>', help='Another optional input string.')
def cli(input_string1, input_string2):
    """
    Outputs messages.
    """
    click.echo("Hello, PyTN!")

@cli.command(name='hello')
def hello():
    """
    Says hello.
    """
    pass

if __name__ == '__main__':
    cli()
