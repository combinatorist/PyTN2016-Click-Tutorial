import click
import sys
import time

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """

@cli.command(name='iterable-bar')
def iterable_bar():
    iterable = range(100)
    with click.progressbar(iterable, file=sys.stdout) as bar:
        for i in bar:
            time.sleep(0.01)

@cli.command(name='explicit-bar')
def explicit_bar():
    iterable = range(100)
    with click.progressbar(iterable, length=len(iterable)) as bar:
        for i in bar:
            time.sleep(0.01)
            bar.update(1)

if __name__ == '__main__':
    cli()

