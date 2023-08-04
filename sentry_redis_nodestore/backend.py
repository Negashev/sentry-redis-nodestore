from __future__ import absolute_import

import os
from base64 import urlsafe_b64encode
from uuid import uuid4

from redis import Redis
from sentry.nodestore.base import NodeStorage
from sentry.utils.kvstore.redis import RedisKVStorage

class RedisNodeStorage(NodeStorage):
    """
    A Redis-based backend for storing node data.
    :param host: Redis server host
    :param port: Redis server port
    :param db: Redis database number
    :param password: Redis server password
    :param default_ttl: How many days keys should be stored (and considered
        valid for reading + returning)
    >>> RedisNodeStorage(
    ...     host='localhost',
    ...     port=6379,
    ...     db=0,
    ...     default_ttl=30,
    ... )
    """

    store_class = RedisKVStorage
    
    default_ttl =None

    def __init__(
        self,
        host='localhost',
        port=6379,
        db=0,
        password=None,
        default_ttl=None,
        **client_options,
        ):
        self.store = self.store_class(Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            client_options=client_options,
        ))
        self.default_ttl = default_ttl
        self.skip_deletes = "_SENTRY_CLEANUP" in os.environ

    def delete(self, id):
        if self.skip_deletes:
            return
        """
        >>> nodestore.delete('key1')
        """
        self.store.delete(id)

    def delete_multi(self, id_list):
        if self.skip_deletes:
            return
        """
        Delete multiple nodes.
        Note: This is not guaranteed to be atomic and may result in a partial delete.
        >>> delete_multi(['key1', 'key2'])
        """
        for id in id_list:
            self.store.delete(id)

    def _get_bytes(self, id):
        """
        >>> nodestore._get_bytes('key1')
        b'{"message": "hello world"}'
        """
        return self.store.get(id)

    def _set_bytes(self, id, data, ttl=None):
        """
        >>> nodestore.set('key1', b"{'foo': 'bar'}")
        """
        self.store.set(id, data, ttl=ttl)

    def generate_id(self):
        return urlsafe_b64encode(uuid4().bytes)
