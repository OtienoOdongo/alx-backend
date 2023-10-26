#!/usr/bin/python3
"""
LIFO (Last-In-First-Out) Cache Placement
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system that implements
    the LIFO (Last-In-First-Out) algorithm.

    Attributes:
        cache_data (dict):
            A dictionary to store cached key-value pairs.
        key_order (list):
            A list to maintain the order in
             which keys were added to the cache.
    """
    def __init__(self):
        """
        Initialize the LIFO cache by calling
        the parent class's constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO strategy.

        Args:
            key (str): The key to be used for caching.
            item: The value to be cached.
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print(f'DISCARD: {self.last_item}')
        if key:
            self.last_item = key

    def get(self, key):
        """
        Retrieve a cached item by its key.

        Args:
            key (str): The key to be used for retrieving the cached item.

        Returns:
            The cached item associated with the key
            or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
