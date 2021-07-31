import os
import pathlib


def main():
    home_path = pathlib.Path.home()
    os.chdir(home_path)
    if os.path.isdir('Desktop'):
        os.chdir('Desktop')
    else:
        os.mkdir('Desktop')
        os.chdir('Desktop')

    if os.path.isdir('Survey'):
        os.chdir('Survey')
    else:
        os.mkdir('Survey')
        os.chdir('Survey')
