import click
import os

@click.command()
def cli():
    """list local files"""
    path= input("Please give the path: ")
    file_list=os.listdir(path)
    print(file_list)
    for entry in file_list:
        print(entry)