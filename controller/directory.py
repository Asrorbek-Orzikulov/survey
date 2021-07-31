import os
import pathlib
# import util


def main():

    home_path = pathlib.Path.home()
    os.chdir(home_path)
    if os.path.isdir('Desktop'):
        os.chdir('Desktop')
        # util.log('success', 'Successfully entered \'Desktop\' folder')

    else:
        # util.log('error', 'Oh silly, looks like the folder \'Desktop\' on your Home folder doesn\'t exist. Let me '
        #                   'create one for you...')
        os.mkdir('Desktop')
        os.chdir('Desktop')
        # util.log('success', 'Successfully entered \'Desktop\' folder')

    if os.path.isdir('Survey'):
        os.chdir('Survey')
        # util.log('success', 'Successfully entered \'Survey\' folder')
    else:
        # util.log('error', 'Oh silly, looks like the folder \'Survey\' on your Desktop folder doesn\'t exist. Let me '
        #                   'create one for you...')
        os.mkdir('Survey')
        os.chdir('Survey')
        # util.log('success', 'Successfully entered \'Survey\' folder')

    # util.log('info', "Now your current path is: " + os.getcwd())
