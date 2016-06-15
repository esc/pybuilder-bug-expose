from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("copy_resources")


default_task = "publish"

@init
def initialize(project):
        project.build_depends_on('mockito')
        project.set_property("copy_resources_target", "$dir_dist")
        project.get_property("copy_resources_glob").append('foo/bar')
        project.install_file("foo/bar", "foo/bar")
