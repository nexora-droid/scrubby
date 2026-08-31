from encodings import utf_8
from typing import Annotated

import typer
import pyfiglet
from pathlib import Path
from colorama import Fore, Style, Back
app = typer.Typer()

@app.command()
def info():
    """Learn more about Scrubby"""
    result = pyfiglet.figlet_format("Scrubby", font='slant')
    print(result)
    print("Scrubby is your friendly helper to scrub through and organise all your files in any directory!")

@app.command()
def ping():
    """Ping Scrubby"""
    print("Pong")

@app.command()
def sort(directory: Annotated[str, typer.Argument(help="Directory to be sorted")],
         dryrun: Annotated[bool, typer.Option('--dryrun', help="Preview what would happen without changing files")] = False):
    """Sort files in certain directory"""
    if not dryrun:
        print("Functionability for this command does not exist")
    else:
        print('YEEHAW')

if __name__ == "__main__":
    app()