#from subprocess import call
import os

#import pkg_resources
import PyInstaller.__main__


def buildExe(pythonFile):

    # create exe file #
    try:
        PyInstaller.__main__.run([
            pythonFile+'.py',
            '--clean',
            '--onefile'
        ]
        )
        
    except Exception as e:
        print(e)

    # remove old file #
    try:
        os.remove(f'binary/{pythonFile}.exe')
    except:
        print('couldnt delete old exe file')


    # move file into base dir #
    try:
        os.rename(f'dist/{pythonFile}.exe', f'binary/{pythonFile}.exe')
    except:
        print('couldnt move new exe file for some reason')


def main():
    files = ['autopressy'] 
    for file in files:
        buildExe(file)




if __name__ == '__main__':
    main()
