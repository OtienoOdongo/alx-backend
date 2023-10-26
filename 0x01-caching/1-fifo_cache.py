#!/usr/bin/python3
"""
using FIFO caching placement policy
Its normally First in First out
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that implements
    a FIFO (First-In-First-Out) algorithm.

    Attributes:
        cache_data (dict):
        A dictionary to store cached key-value pairs.
    """

    def __init__(self):
        """
        Initializes the FIFO cache by calling
        the parent class's constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add a key-value pair to the cache.

        If either the key or the item is None,
        this method does nothing.
        If the number of items in the cache exceeds
        the maximum allowed (MAX_ITEMS),
        the method discards the first item
        added using FIFO and prints a discard message.

        Args:
            key: The key to be used for caching.
            item: The value to be cached.
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        self.cache_data[key] = item

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
