#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,"""

from fabric.api import *
from datetime import datetime
from os.path import isfile

env.hosts = ['100.25.193.17', '54.160.116.235']
env.user = "ubuntu"

def do_deploy(archive):
    """ Function that distributes an archive to your web servers """
    if isfile(archive) is False:
        return False
    try:
        put(archive, "/tmp/")
        file = archive.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False