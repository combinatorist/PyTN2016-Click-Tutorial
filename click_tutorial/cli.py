import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """
    pass

@cli.command(name='prompt1')
@click.option('--data', prompt=True)
def prompt1_ish(data):
    click.echo('data: ' + str(data))

@cli.command(name='prompt2')
@click.option('--data', prompt=True)
def prompt2_ish(data):
    click.echo('Custom prompt text: ' + str(data))

if __name__ == '__main__':
    cli()

