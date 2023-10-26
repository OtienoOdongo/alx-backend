#!/usr/bin/python3
"""
using FIFO caching placement policy
Its normally First in First out
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that implements
    FIFO (First-In-First-Out) algorithm

    Attributes:
        cache_data (dict):
         A dictionary to store cached key-value pairs.
    """

    def __init__(self):
        """
        Initialize the FIFO cache by calling
        the parent class's constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key to be used for caching.
            item: The value to be cached.
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_added_key = sorted(self.cache_data)[0]
            self.cache_data.pop(first_added_key)
            print(f'DISCARD: {first_added_key}')

    def get(self, key):
        """
        Retrieve a cached item by its key.

        If the key is None or does not exist in the cache,
         it returns None.

        Args:
            key:
            The key to be used for retrieving the cached item.

        Returns:
            The cached item associated with the key,
            or None if the key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
