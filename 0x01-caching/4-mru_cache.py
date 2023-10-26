#!/usr/bin/python3
"""
MRU cache placement
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used (MRU) caching system.
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init()
        self.recent_items = []

    def put(self, key, item):
        """
        Add an item to the cache using the MRU strategy.

        Args:
            key (str): The key to be used for caching.
            item: The value to be cached.
        """
        if key and item:
            if self.cache_data.get(key):
                self.recent_items.remove(key)
            while len(self.recent_items) >= self.MAX_ITEMS:
                discarded_key = self.recent_items.pop()
                self.cache_data.pop(discarded_key)
                print(f'DISCARD: {discarded_key}')
            self.recent_items.append(key)
            self.cache_data[key] = item

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
        if self.cache_data.get(key):
            self.recent_items.remove(key)
            self.recent_items.append(key)
        return self.cache_data.get(key)
