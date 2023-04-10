#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
 from the contents of the web_static """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function that generates a .tgz archive
    from the contents of the web_static """

    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    local("tar -cvzf {} web_static".format(file))


if __name__ == "__main__":
    do_pack()