import click

COLORS = ['white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']

@click.group(name="pytn")
def cli():
    """
    Output a greeting to PyTennessee!
    """

@cli.command(name="echo")
@click.option('--err', default=False)
@click.option('--new-line/--no-new-line', default=True)
def echo_ish(err, new_line):
    click.echo("Say what you need to say.")
    click.echo("This is a message.", nl=new_line, err=err)
    click.echo("This should always go to standard error.", err=True)
    # you can demo stderr by redirecting stdout with $ pytn echo > deleteme.txt
    # or, to redirect stderr: $ pytn echo 2> deleteme.txt

@cli.command()
@click.option('--fg', type=click.Choice(COLORS))
def style(fg):
    click.echo(click.style("This is a message.", fg=fg))

@cli.command()
@click.option('--fg', type=click.Choice(COLORS))
def secho(fg):
    click.echo(click.style("This is a message.", fg=fg))

if __name__ == '__main__':
    cli()

