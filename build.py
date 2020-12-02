#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task, depends
from os import path
from subprocess import call

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "cs3280Project5"
default_task = "publish"

target_dir = path.join('target', 'dist', 'app')

@init
def set_properties(project):
    project.build_depends_on('mockito')

@init
def normalize_target_dir(project):
    project.set_property('dir_dist', target_dir)

@init
def copy_html_pages_to_distribution(project):
    project.set_property('copy_resources_target', target_dir)
    project.set_property('copy_resources_glob', ['*.html', '*.HTML', '*.htm', '*.HTM'])

@depends('publish')
@task
def launch_server(project):
    print("Note: This webserver is not running in a container.")
    print("Note: A webpage should be available at http://127.0.0.1:3280/index.html")
    call([
        'python',
        path.join(target_dir, 'server.py')
    ])
