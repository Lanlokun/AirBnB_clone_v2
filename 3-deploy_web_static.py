#!/usr/bin/python3
""" Fabric script that creates and distributes an archive
to your web servers, using the function do_deploy """
from fabric.api import local, put, run, env
from os.path import isfile
from datetime import datetime
env.hosts = ['100.25.193.17', '54.160.116.235']
env.user = "ubuntu"


def do_pack():
    """ Function that generates a .tgz archive
    from the contents of the web_static """

    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    local("tar -cvzf {} web_static".format(file))


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


def deploy():
    """ Function that creates and distributes
an archive to your web servers """
    archive = do_pack()
    print(archive)
    if archive is None:
        print("No archive")
        return False
    return do_deploy(archive)
