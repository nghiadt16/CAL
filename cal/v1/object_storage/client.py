from cal import conf
from cal.base import BaseClient
from cal.v1.object_storage.drivers.base import BaseDriver

CONF = conf.CONF


class Client(BaseClient, BaseDriver):
    """Top-level object to access CAL API
    This class must be extended base.Singleton class to make
    sure only one instance of this one is ever created."""

    def __init__(self, provider, *args, **kwargs):
        BaseClient.__init__(self, CONF.object_storage.driver_path, provider)
