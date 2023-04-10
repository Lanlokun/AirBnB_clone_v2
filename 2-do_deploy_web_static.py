#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,"""

from fabric.api import env, put, run, local
from datetime import datetime
from os.path import isfile
from os import path

env.hosts = ['100.25.193.17', '54.160.116.235']
env.user = "ubuntu"


def do_deploy(archive):
    """ Function that distributes an archive to your web servers """
    if isfile(archive) is False:
        print("File not found")
        return False
    try:
        put(archive, "/tmp/")
        print("File uploaded")
        file = archive.split("/")[-1]
        print(file)
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        print(folder)
        run("mkdir -p {}".format(folder))
        print("Folder created")
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        print("Uncompressed")
        run("rm /tmp/{}".format(file))
        print("File deleted")
        run("mv {}/web_static/* {}".format(folder, folder))
        print("Moved")
        run("rm -rf {}/web_static".format(folder))
        print("Removed")
        run("rm -rf /data/web_static/current")
        print("Removed")
        run("ln -s {} /data/web_static/current".format(folder))
        print("Linked")
        print("New version deployed!")
        return True
    except Exception:
        return False
