from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "flappy_bird"
default_task = "publish"

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "path/to/your/code")
    project.set_property("source_dist_ignore_patterns", ["**/*.pyc", "**/__pycache__"])
