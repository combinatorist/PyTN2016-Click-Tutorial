import click

CHOICES = ['a', 'b', 'c', 'd']

@click.command(name='pytn')
@click.option('--letter', type=click.Choice(CHOICES))
@click.option('--number', type=click.IntRange(0, 100))
@click.option('--clamped-number', type=click.IntRange(0, 100, clamp=True))
def cli(letter, number, clamped_number):
    """
    Output a greeting to PyTennessee!
    """
# for some reason this works when I comment out the 'letter' line    
# it works if you specify letter, but not if you only specificy number
# fixed - the issue was that the letter argument was read in as "None".
# So, I had to convert to str before I could append it into the string.
    click.echo("letter: " + str(letter))
    click.echo("number: " + str(number))
    click.echo("clamped_number: " + str(clamped_number))
    click.echo("Hello, PyTN!")

if __name__ == '__main__':
    cli()
