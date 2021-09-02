
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
CAIRO is a code for artificially intelligent reactor operation.
"""
from tarot.ver import get_git_version
# from cairo.lorenz import *
# from cairo.optimizers import *
# from cairo.sunrise import *
# from cairo.tools import *


try:
    __version__ = get_git_version()
except (ValueError, IOError):
    __version__ = '1.0'
