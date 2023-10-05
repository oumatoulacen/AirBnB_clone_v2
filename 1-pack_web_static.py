#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive from the contents
of the web_static folder '''

from fabric.api import local, run, put
from datetime import datetime
import os

def do_pack():
    ''' archive from the contents of the web_static'''
    env.hosts = ['100.26.167.149	','100.25.163.174']
    env.user = ubuntu
    now = datetime.now()
    now = now.strftime("%Y%m%d%H%M%S")

    os.makedirs("versions")
    archive_name = "web_static_{}.tgz".format(now)
    local("tar -cvzf versions/{} web_static".format(archive_name))
    return "versions/{}".format(archive_name)

