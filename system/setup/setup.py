import sys
import subprocess
import os

def check_os():
    if sys.platform == "linux" or sys.platform == "linux2":
        print "Detected a linux distribution, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a Virtual Environtment through virtualenv"

    elif sys.platform == "darwin":
        print "Detected OSX, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a Virtual Environtment through virtualenv"
        else:
            print "*****YOU ARE NOT USING A VIRTUAL ENVIRONMENT*****"
            print "Create a virtual environment before rerunning the setup"
            subprocess.call("pwd", shell=True)
            subprocess.call("virtualenv ./../../pylotVenv", shell=True)
            os.system("bash --rcfile setupOSX.sh")
        subprocess.call("pip install -r dependenciesOSX.txt", shell=True)
    elif sys.platform == "win32" or sys.platform == "win64":
        print "Detected Windows, running the appropriate installation"
        if hasattr(sys, 'real_prefix'):
            print "Detected that we are already using a Virtual Environtment through virtualenv"
    else:
        print "Sorry we don't support your OS at this time"

check_os()
