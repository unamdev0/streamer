import os
import subprocess
import sys
import argparse
import re
from bs4 import BeautifulSoup
import requests 

preUrl = "https://indiaprox.org"
postUrl="/0/7/0"

def scrape(url,search):
    request = requests.get(url)
    
    soup = BeautifulSoup(request.content, 'html.parser')
    page = soup.findAll("a")

    for i in page:
        if search in i.get('href'):
            return i.get('href')


def runCommand(command):
    
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,shell=True)
    return iter(p.stdout.readline, b'')



def checkEpisode(episode=None):
    if(episode==None):
        return False
    matchObj = re.match( r'^s[0-9][1-9]e[0-9]{2,3}$',episode)
    if matchObj:
        return True
    else:
        return False

def link(url):
    try:
        command="peerflix \""+url.strip()+"\" --vlc --fullscreen"
        os.system(command)
    except KeyboardInterrupt:
        print('Exiting streamer...\nSee you soon :)\n')

def movie(name,quality=None):
    try:
        name=name.replace(' ','%20')
        if quality:
            name = name+"%20"+quality
        url = preUrl+"/search/"+name+postUrl
        parseUrl =scrape(url,'/torrent/')
        url = preUrl+parseUrl
        torrent = scrape(url,'magnet:')
        link(torrent)
    except KeyboardInterrupt:
        print('Exiting streamer...\nSee you soon :)\n')

    

def series(name,episode,quality=None):
    try:
        name=name.replace(' ','%20')
        name=name+"%20"+episode
        if quality:
            name = name+"%20"+quality
        url = preUrl+"/search/"+name+postUrl
        parseUrl =scrape(url,'/torrent/')
        url = preUrl+parseUrl
        torrent = scrape(url,'magnet:')
        link(torrent)
    except KeyboardInterrupt:
        print('Exiting streamer...\nSee you soon :)\n')


    
def checkDependency():
    try:
        command ="npm --version"

                        ##----------------Checking for NPM----------------

        for line in runCommand(command):
            if ("'npm' is not recognized as an internal or external command," in str(line)):
                print("Please install NPM and run the program again. :) ")
                return False
            
                        ##----------------Checking for required module----------------

        command ="npm list -g peerflix"
        for line in runCommand(command):
            if("-- (empty)" in str(line)):
                print("Package not Found")
                print("Run the following command in order to install package")
                print("npm install -g peerflix")
                return False
        print("\n\n-------------------All requirement satisfied-------------------\n\n")
        return True
    except KeyboardInterrupt:
        print('Exiting streamer...\nSee you soon :)\n')


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
        if(checkEpisode(args.episode)):
            series(args.name,args.episode,args.quality)
        else:
            print("Please provide valid episode in format=> s01e01\n")
            exit(0)
    elif(args.type=='link'):
        args.name= "\""+args.name+"\""
        link(args.name)
    else:
        print("Please select one of the following as argument for 'type' \nmovie\nseries\nlink")
        exit(0)
    

if __name__=="__main__":
    check=checkDependency()
    if(check==False):
        exit(0)
    startApp()
        
        
        
    
