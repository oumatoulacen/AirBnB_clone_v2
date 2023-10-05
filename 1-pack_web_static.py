#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive from the contents
of the web_static folder '''
from fabric.api import local
from fabric.decorators import task


@task
def do_pack():
    ''' archive from the contents of the web_static'''
    local("mkdir versions; tar -cvzf versions/web_static_$(date \
            +%Y%m%d%H%M%S).tgz web_static/")
