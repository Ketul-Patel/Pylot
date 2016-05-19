import sys
import subprocess
import os

def _setup():
    subprocess.call("pwd", shell=True)
    if sys.platform == "linux" or sys.platform == "linux2":
        print "Detected a linux distribution, running the appropriate installation"
        if "Ubuntu" in sys.platform.linux_distribution():
            if hasattr(sys, 'real_prefix'):
                print "Detected that we are already using a Virtual Environtment through virtualenv"
                print "Installing dependencies in Virtual Environment"
                subprocess.call("pip install -r system/setup/dependenciesUbuntu.txt", shell=True)
            else:
                print "You do not have a Virtual Environment set up. You should set one up for your project."
                print "Would you like for us to create one for you? [Y/N]"
                user_input = raw_input()
                if user_input.lower() == "y":
                    print "Ok creating a Virtual Environment. Please rerun python setup.py after the Virtual Environment is created"
                    subprocess.call("virtualenv pylotVenv", shell=True)
                    os.system("bash --rcfile system/setup/setupUbuntu.sh")
                else:
                    print "Aborting setup. Please create a Virtual Environment and then rerun python setup.py"
                    return None
        else:
            print "Sorry we only support Ubuntu at this time. Please setup manually."
            return None
    elif sys.platform == "darwin":
        print "Detected OSX, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a Virtual Environtment through virtualenv"
            print "Installing dependencies in Virtual Environment"
            subprocess.call("pip install -r system/setup/dependenciesOSX.txt", shell=True)
        else:
            print "You do not have a Virtual Environment set up. You should set one up for your project."
            print "Would you like for us to create one for you? [Y/N]"
            user_input = raw_input()
            if user_input.lower() == "y":
                print "Ok creating a Virtual Environment. Please rerun python setup.py after the Virtual Environment is created"
                subprocess.call("virtualenv pylotVenv", shell=True)
                os.system("bash --rcfile system/setup/setupOSX.sh")
            else:
                print "Aborting setup. Please create a Virtual Environment and then rerun python setup.py "
                return None
    elif sys.platform == "win32" or sys.platform == "win64":
        print "Detected Windows, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a Virtual Environtment through virtualenv"
    else:
        print "Sorry we don't support your OS at this time"

_setup()
