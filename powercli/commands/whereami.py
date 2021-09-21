import click
import os

@click.command()
def cli():
    my_location=os.getcwd()
    click.echo(my_location)