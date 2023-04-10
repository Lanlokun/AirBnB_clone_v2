#!/usr/bin/python3
""" Fabric script that that deletes out-of-date archives, using the function """

from fabric.api import *
from datetime import datetime
from os.path import isfile, getsize


env.hosts = ['100.25.193.17', '54.160.116.235']
env.user = "ubuntu"

def do_clean(number=0):
    """ Function that deletes out-of-date archives """
    number = int(number)
    if number == 0 or number == 1:
        local("ls -t versions | tail -n +2 | xargs rm -rf")
    elif number >= 2:
        local("ls -t versions | tail -n +{} | xargs rm -rf".format(number))
    else:
        print("Number must be an integer greater than 0")
        return False
    with cd("/data/web_static/releases"):
        files = run("ls -t | tail -n +2")
        print(files)
        for file in files:
            run("rm -rf {}".format(file))

    
