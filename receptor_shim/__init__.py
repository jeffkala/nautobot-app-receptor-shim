"""App declaration for receptor_shim."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class ReceptorShimConfig(NautobotAppConfig):
    """App configuration for the receptor_shim app."""

    name = "receptor_shim"
    verbose_name = "Receptor Shim"
    version = __version__
    author = "Jeff Kala"
    description = "Receptor Shim."
    base_url = "receptor-shim"
    required_settings = []
    min_version = "2.1.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = ReceptorShimConfig  # pylint:disable=invalid-name
