#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive from the contents
of the web_static folder '''
from fabric.api import local, run, put
from fabric.decorators import task


@task
def do_pack():
    ''' archive from the contents of the web_static'''
    local("mkdir versions; tar -cvzf versions/web_static_$(date \
            +%Y%m%d%H%M%S).tgz web_static/")


env.host = ['100.25.163.174', '100.26.167.149']
env.user = ubuntu


@task
def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    try:
        name_with_ext = archive_path.split("/")[-1]
        name_without_ext = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            name_with_ext, name_without_ext))
        run('rm -rf /tmp/{}'.format(name_with_ext))
        run('rm /data/web_static/current')
        run('ln -s /data/web_static/releases/{} \
                /data/web_static/current'.format(name_without_ext))
        return True
    except Exception:
        return False
