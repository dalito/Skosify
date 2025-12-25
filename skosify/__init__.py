from importlib.metadata import PackageNotFoundError, version

from .skosify import skosify
from .config import config
from . import infer, check

__all__ = ['skosify', 'config', 'infer', 'check']

try:
    __version__ = version("skosify")
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    try:
        from ._version import version as __version__
    except ImportError:
        __version__ = "0.0.0"