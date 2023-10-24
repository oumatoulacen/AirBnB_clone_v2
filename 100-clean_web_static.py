# #!/usr/bin/python3
# """ Function that deploys """
# from fabric.api import *
# from fabric.decorators import task
# from datetime import datetime
# import os

# env.hosts = ["100.25.163.174", "100.26.167.149"]


# @task
# def do_clean(number=0):
#     """formats input and cleans remote"""
#     n = 1
#     if int(number) != 0:
#         n = int(number)
#     pth = "/data/web_static/releases/*"
#     local("ls -dt ./versions/* | head -n -{} | xargs rm -fr".format(n))
#     run("ls -dt {} | head -n -{} | xargs rm -fr".format(pth, n))
