import sys
import subprocess
import os
import platform

def _setup():
    if sys.platform == "linux" or sys.platform == "linux2":
        print "Detected a linux distribution, running the appropriate installation"
        print "--------------------------"
        if "Ubuntu" in platform.linux_distribution():
            if hasattr(sys, 'real_prefix'):
                print "Detected that we are already using a virtual environtment through virtualenv"
                print "Installing dependencies in virtual environment"
                subprocess.call("pip install -r system/setup/dependenciesUbuntu.txt", shell=True)
            else:
                print "Checking for an inactive virtual environment"
                if os.path.exists(os.path.join(os.getcwd(), "pylotVenv")):
                    print "Found pylotVenv, activating the virtual environment"
                    print "Now that you are setup please run:"
                    print "--------------------------"
                    print "python manage.py runserver"
                    print "--------------------------"
                    print "To start the server. For more information on how to get started please visit the Github Wiki"
                    os.system("bash --rcfile system/setup/setupUbuntu.sh")
                else:
                    print "You do not have a virtual environment set up. You should set one up for your project. If you have already created a virtual environment under a different name that you would like to use please source the virtualenv manually."
                    print "Would you like for us to create one for you? [y/n]"
                    user_input = raw_input()
                    if user_input.lower() == "y":
                        print "Ok creating a virtual environment. Please rerun python setup.py after the virtual environment is created and activated"
                        subprocess.call("virtualenv pylotVenv", shell=True)
                        os.system("bash --rcfile system/setup/setupUbuntu.sh")
                    else:
                        print "Aborting setup. please create a virtual environment and then rerun python setup.py"
                        return None
        else:
            print "Sorry we only support ubuntu at this time. Please setup manually."
            print "virtualenv pylotVenv"
            print "source pylotVenv/scripts/activate"
            print "pip install -r system/setup/dependenciesUbuntu.txt"
            return None
    elif sys.platform == "darwin":
        print "Detected osx, running the appropriate installation"
        print "--------------------------"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a virtual environtment through virtualenv"
            print "Installing dependencies in virtual environment"
            subprocess.call("pip install -r system/setup/dependenciesOSX.txt", shell=True)
        else:
            print "Checking for an inactive virtual environment"
            if os.path.exists(os.path.join(os.getcwd(), "pylotVenv")):
                print "Found pylotVenv, activating the virtual environment. If you still need to install dependencies then simply run python setup.py again."
                print "Now that you are setup please run:"
                print "--------------------------"
                print "python manage.py runserver"
                print "--------------------------"
                print "To start the server. For more information on how to get started please visit the Github Wiki"
                os.system("bash --rcfile system/setup/setupOSX.sh")
            else:
                print "You do not have a virtual environment set up. you should set one up for your project. If you have already created a virtual environment under a different name that you would like to use please source the virtualenv manually."
                print "Would you like for us to create one for you? [y/n]"
                user_input = raw_input()
                if user_input.lower() == "y":
                    print "Ok creating a virtual environment. Please rerun python setup.py after the virtual environment is created and activated."
                    subprocess.call("virtualenv pylotVenv", shell=True)
                    os.system("bash --rcfile system/setup/setupOSX.sh")
                else:
                    print "Aborting setup. Please create a virtual environment and then rerun python setup.py "
                    return None
    elif sys.platform == "win32" or sys.platform == "win64":
        print "detected windows, please follow the instructions below to complete the installation"
        print "--------------------------"
        print "don't have a pylot virtualenv?  run these commands: (in a bash terminal)"
        print "python -m virtualenv pylotVenv"
        print "source pylotVenv/scripts/activate"
        print "pip install -r system/setup/dependenciesPC.txt"
        print ""
        print "please note that git bash uses a cache - if your print statements don't work try 'conemu' terminal or similar"
    else:
        print "Sorry we don't support your OS at this time"
        print "--------------------------"
        print "Try running the following steps (accounting for your operating system) to complete the installation"
        print "python -m virtualenv pylotVenv"
        print "source pylotVenv/scripts/activate"
        print "pip install -r system/setup/dependenciesOSX.txt"
        return None
    print "Now that you are setup please run:"
    print "--------------------------"
    print "python manage.py runserver"
    print "--------------------------"
    print "To start the server. For more information on how to get started please visit the Github Wiki"

_setup()
