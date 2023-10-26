#!/usr/bin/python3
"""
MRU cache placement
"""


from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class CustomMRUCache(BaseCaching):
    """
    Custom implementation of Most Recently Used (MRU)
    caching system.
    """

    def __init__(self):
        """
        Initialize the custom MRU cache.
        """
        super().__init__()
        self.__custom_keys = []
        self.__custom_rlock = RLock()

    def put(self, key, item):
        """
        Add an item to the cache using the MRU strategy.

        Args:
            key (str): The key to be used for caching.
            item: The value to be cached.
        """
        if key is not None and item is not None:
            key_out = self._balance(key)
            with self.__custom_rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print(f'DISCARD: {key_out}')

    def get(self, key):
        """
        Retrieve a cached item by its key.

        Args:
            key (str):
            The key to be used for retrieving the cached item.

        Returns:
            The cached item associated with the key,
            or None if the key is not found.
        """
        with self.__custom_rlock:
            value = self.cache_data.get(key, None)
            if key in self.__custom_keys:
                self._balance(key)
        return value

    def _balance(self, key_in):
        """
        Perform the MRU balancing logic.
        """
        key_out = None
        with self.__custom_rlock:
            keys_length = len(self.__custom_keys)
            if key_in not in self.__custom_keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = self.__custom_keys.pop(keys_length - 1)
                    self.cache_data.pop(key_out)
            else:
                self.__custom_keys.remove(key_in)
            self.__custom_keys.insert(keys_length, key_in)
        return key_out
