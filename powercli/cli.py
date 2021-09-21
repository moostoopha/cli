import click
import os
import six
import logging
import boto3
from pyfiglet import figlet_format

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"powercli.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli




@click.command(cls=ComplexCLI)
def cli():
    """
    +-++-++-++-++-++-++-++-+
    |P||O||W||E||R||C||L||I|
    +-++-++-++-++-++-++-++-+

                               Welcome to Power CLI
    """
    pass
#     log("Power CLI", color="blue", figlet=True)
#     log("               Welcome to Power CLI", "green")
#
#
# def log(string, color, font="slant", figlet=False):
#     if colored:
#         if not figlet:
#             six.print_(colored(string, color))
#         else:
#             six.print_(colored(figlet_format(
#                 string, font=font), color))
#     else:
#         six.print_(string)
