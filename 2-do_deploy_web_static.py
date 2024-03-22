#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ["54.175.254.121", "18.204.20.200"]  # <IP web-01>, <IP web-02>


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        no_extension = archive_name.split('.')[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, no_extension))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(no_extension, no_extension))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_extension))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_extension))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
