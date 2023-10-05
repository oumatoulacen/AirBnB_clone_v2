#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive from the contents
of the web_static folder '''

from fabric.api import local, run, put

def do_pack():
    ''' archive from the contents of the web_static'''
    local('ls')

