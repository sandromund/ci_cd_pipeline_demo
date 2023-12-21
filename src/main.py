"""
Entry point of the program.
"""
import click

from util import addition


@click.command()
@click.option('--number_x',
              default=1,
              help='Enter a float value',
              type=float)
@click.option('--number_y',
              default=1,
              help='Enter a float value',
              type=float)
def main(number_x, number_y):
    """
    Add two numbers together and echos the result to stout.

    :param number_x: first number
    :param number_y: second number
    :return: String, the calculation
    """
    click.echo(f"x={number_x} + y={number_y} == {addition(number_x, number_y)}")


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
