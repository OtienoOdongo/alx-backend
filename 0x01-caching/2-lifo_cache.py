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
        custom_stack (list):
            A list to maintain the order in
             which keys were added to the cache.
    """

    def __init__(self):
        """
        Initialize the LIFO cache by calling
        the parent class's constructor.
        """
        super().__init__()
        self.custom_stack = []

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO strategy.

        Args:
            key (str): The key to be used for caching.
            item: The value to be cached.
        """
        if key is None or item is None:
            pass

        if key in self.cache_data:
            self.custom_stack.remove(key)

        while len(self.custom_stack) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.custom_stack.pop()
            self.cache_data.pop(discarded_key)
            print(f'DISCARD: {discarded_key}')

        self.custom_stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve a cached item by its key.

        If the key is None or does not exist in the cache,
        it returns None.

        Args:
            key (str):
            The key to be used for retrieving the cached item.

        Returns:
            The cached item associated with the key,
             or None if the key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
