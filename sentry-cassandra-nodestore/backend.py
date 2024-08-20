from .casscache import Client  # NOQA

from sentry.nodestore.base import NodeStorage
from sentry.utils.cache import memoize

class CassandraNodeStorage(NodeStorage):
    """
    A Cassandra-based backend for storing node data.

    >>> CassandraNodeStorage(
    ...     servers=['127.0.0.1:9042'],
    ...     keyspace='sentry',
    ...     columnfamily='nodestore',
    ... )
    """

    def __init__(
        self,
        servers,
        keyspace='sentry',
        columnfamily='nodestore',
        **kwargs
    ):
        self.servers = servers
        self.keyspace = keyspace
        self.columnfamily = columnfamily
        self.options = kwargs
        super(CassandraNodeStorage, self).__init__()

    @memoize
    def connection(self):
        return Client(
            servers=self.servers,
            keyspace=self.keyspace,
            columnfamily=self.columnfamily,
            **self.options
        )

    def _get_bytes(self, id):
        return self.connection.get(id)

    def _get_bytes_multi(self, id_list):
        return self.connection.get_multi(id_list)

    def _set_bytes(self, id, data, ttl=None):
        self.connection.set(id, data)

    def delete(self, id):
        self.connection.delete(id)
        self._delete_cache_item(id)

    def delete_multi(self, id_list):
        self.connection.delete_multi(id_list)
        self._delete_cache_items(id_list)

    def bootstrap(self):
        pass