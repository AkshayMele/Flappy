from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

unittest_test_source = "src/unittest/python"
default_task = "publish"
