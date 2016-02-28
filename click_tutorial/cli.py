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

@cli.command()
@click.option('--data', prompt="Password", confirmation_prompt=True, hide_input=True)
def prompt4(data):
    click.echo('password: ' + data)

@cli.command()
@click.confirmation_option(prompt="Are you sure?")
def prompt5():
    click.echo("Doing something...")

if __name__ == '__main__':
    cli()


