import os
import subprocess
import sys
import argparse

def run_command(command):
    
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,shell=True)
    
    return iter(p.stdout.readline, b'')

def checkDependency():
    
    command ="npm --version"

                    ##----------------Checking for NPM----------------

    for line in run_command(command):
        if ("'npm' is not recognized as an internal or external command," in str(line)):
            print("Please install NPM and run the program again. :) ")
            return False
        
                    ##----------------Checking for required module----------------

    command ="npm list -g peerflix"
    for line in run_command(command):
        if("-- (empty)" in str(line)):
            print("Package not Found")
            print("Run the following command in order to install package")
            print("npm install -g peerflix")
            return False
    print("\n\n-------------------All requirement satisfied-------------------\n\n")
    return True

def startApp():

    
    parser = argparse.ArgumentParser(description='Watch movies from torrent direcly without downloading')

                    ##----------------Type of file----------------

    parser.add_argument('type',type=str,help='Type of file, i.e. movie,series or link')

                    ##----------------Name of file----------------

    parser.add_argument('name',type=str,help='Name of the file to be watched')

                    ##----------------Episode of series----------------


    parser.add_argument('--episode',type=str,help=' To specify episode of the series')

                    ##----------------quality of file----------------


    parser.add_argument('--quality',type=str,help='To specify quality')
   
    args = parser.parse_args()

    if (args.type=='movie'):
        movie(args.name,args.quality)
    elif(args.type=='series'):
        checkepisode(args.episode)
        series(args.name,args.episode,args.quality)
    elif(args.type=='link'):
        link()
    else:
        print("Please select one of the following as argument for 'type' \nmovie\nseries\nlink")
        exit(0)
    

if __name__=="__main__":
    check=checkDependency()
    if(check==False):
        exit(0)
    startApp()
        
        
    
