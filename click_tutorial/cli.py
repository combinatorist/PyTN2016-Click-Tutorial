import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """
    pass

@cli.command()
@click.option('--data', prompt=True)
def prompt1(data):
    click.echo('data: ' + str(data))

@cli.command(name='prompt2')
@click.option('--data', prompt="Custom prompt text")
def prompt2_ish(data):
    click.echo('data: ' + str(data))

@cli.command()
@click.option('--data', prompt="Password", hide_input=True, confirmation_prompt=True)
def prompt3(data):
    click.echo('password: ' + data)
if __name__ == '__main__':
    cli()

