import click
import sys

@click.command()
@click.option('--words', default='Hello')
@click.argument('name')
def greet(name, words):
    click.echo(f'{words}, {name}!')

    
if __name__ == '__main__':
    # args = sys.argv
    # for arg in args:
    #     print(arg)
    greet()