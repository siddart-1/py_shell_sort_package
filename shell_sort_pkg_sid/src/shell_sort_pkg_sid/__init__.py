# read version from installed package
from importlib.metadata import version
from .shell_sort import shell_sort
__version__ = version("shell_sort_package")