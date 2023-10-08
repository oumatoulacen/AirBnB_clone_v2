#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
import fabric
from fabric.decorators import task
from fabric.api import *
import os

env.hosts = ["100.25.163.174", "100.26.167.149"]


@task
def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        with_ext = archive_path.split("/")[-1]
        without_ext = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/" + without_ext)
        run("tar -xzf /tmp/{} -C /data/web_static/releases/\
{}".format(with_ext, without_ext))
        run("rm /tmp/{}".format(with_ext))
        run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".format(without_ext, without_ext))
        run("rm -rf /data/web_static/releases/{}/web_static\
".format(without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
/data/web_static/current".format(without_ext))
        return True
    except Exception:
        return False


@task
def do_pack():
    """generates a .tgz archive from web_static"""
    datestr = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(datestr)
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static/".format(file_name)).succeeded:
        return file_name
    return None
