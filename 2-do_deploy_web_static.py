# #!/usr/bin/python3
# """ Fabric script that generates a .tgz archive """
# from fabric import task
# from fabric.api import *
# from datetime import datetime
# import os

# env.hosts = ["100.25.163.174", "100.26.167.149"]


# @task
# def deploy(c):
#     """ Fabric script that creates and distributes an archive """
#     file_name = do_pack()
#     if file_name is None:
#         return False
#     return do_deploy(c, file_name)


# @task
# def do_deploy(c, archive_path):
#     """Fabric script that distributes an archive to web servers"""
#     try:
#         if not os.path.exists(archive_path):
#             return False
#         with_ext = archive_path.split("/")[-1]
#         without_ext = archive_path.split("/")[-1].split(".")[0]
#         pth = "/data/web_static/releases/"
#         put(archive_path, "/tmp/")
#         run("mkdir -p " + pth + without_ext)
#         run("tar -xzf /tmp/{} -C {}{}/".format(with_ext, pth, without_ext))
#         run("rm /tmp/{}".format(with_ext))
#         run("mv {1}{0}/web_static/* {1}{0}/".format(without_ext, pth))
#         run("rm -rf {}{}/web_static".format(pth, without_ext))
#         run("rm -rf /data/web_static/current")
#         run("ln -s {}{}/ /data/web_static/current".format(pth, without_ext))
#         return True
#     except Exception:
#         return False


# @runs_once
# def do_pack():
#     """generates a .tgz archive from web_static"""
#     datestr = datetime.now().strftime("%Y%m%d%H%M%S")
#     file_name = "versions/web_static_{}.tgz".format(datestr)
#     local("mkdir -p versions")
#     if local("tar -cvzf {} web_static/".format(file_name)).succeeded:
#         return file_name
#     return None
