import sys
import subprocess
import os
import platform

def _setup():
    if sys.platform == "linux" or sys.platform == "linux2":
        print "detected a linux distribution, running the appropriate installation"
        if "ubuntu" in platform.linux_distribution():
            if hasattr(sys, 'real_prefix'):
                print "detected that we are already using a virtual environtment through virtualenv"
                print "installing dependencies in virtual environment"
                subprocess.call("pip install -r system/setup/dependenciesubuntu.txt", shell=True)
            else:
                print "you do not have a virtual environment set up. you should set one up for your project."
                print "would you like for us to create one for you? [y/n]"
                user_input = raw_input()
                if user_input.lower() == "y":
                    print "ok creating a virtual environment. please rerun python setup.py after the virtual environment is created"
                    subprocess.call("virtualenv pylotvenv", shell=True)
                    os.system("bash --rcfile system/setup/setupubuntu.sh")
                else:
                    print "aborting setup. please create a virtual environment and then rerun python setup.py"
                    return none
        else:
            print "sorry we only support ubuntu at this time. please setup manually."
            return none
    elif sys.platform == "darwin":
        print "detected osx, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "detected that we are already using a virtual environtment through virtualenv"
            print "installing dependencies in virtual environment"
            subprocess.call("pip install -r system/setup/dependenciesosx.txt", shell=True)
        else:
            print "you do not have a virtual environment set up. you should set one up for your project."
            print "would you like for us to create one for you? [y/n]"
            user_input = raw_input()
            if user_input.lower() == "y":
                print "ok creating a virtual environment. please rerun python setup.py after the virtual environment is created"
                subprocess.call("virtualenv pylotvenv", shell=True)
                os.system("bash --rcfile system/setup/setuposx.sh")
            else:
                print "aborting setup. please create a virtual environment and then rerun python setup.py "
                return none
    elif sys.platform == "win32" or sys.platform == "win64":
        print "detected windows, please follow the instructions below to complete the installation"
        print "don't have a pylot virtualenv?  run these commands: (in a bash terminal)"
        print "python -m virtualenv pylotvenv"
        print "source pylotvenv/scripts/activate"
        print "pip install -r system/setup/dependenciesPC.txt"
        print ""
        print "please note that git bash uses a cache - if your print statements don't work try 'conemu' terminal or similar"
    else:
        print "Sorry we don't support your OS at this time"
        print "Try running the following steps (accounting for your operating system) to complete the installation"
        print "python -m virtualenv pylotvenv"
        print "source pylotvenv/scripts/activate"
        print "pip install -r system/setup/dependenciesOSX.txt"

_setup()
