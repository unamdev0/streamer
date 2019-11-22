import os
import subprocess
import sys



def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,shell=True)
    return iter(p.stdout.readline, b'')

def checkDependency():
    command ="npm --version"
    for line in run_command(command):
        if ("'npm' is not recognized as an internal or external command," in str(line)):
            print("Please install NPM and run the program again. :) ")
            return False
            
        else:
            print("Checking for required package")

    command ="npm list -g peerflix"
    for line in run_command(command):
        if("-- (empty)" in str(line)):
            print("Package not Found")
            print("Run the following command in order to install package")
            print("npm install -g peerflix")
            return False
            
    return True


if __name__=="__main__":
    check=checkDependency()
    if(check==True):
        exit(0)
    else:
        type = sys.argv[0]
        name  = sys.argv[1]
        
        if (type = "series")
        
        
    
