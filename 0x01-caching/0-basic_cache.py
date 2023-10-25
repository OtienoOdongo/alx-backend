#!/usr/bin/env python3
"""
Basic Dictionary cache implementation
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a basic dictionary caching system
    """
    def put(self, key, item):
        """
        a method that adds items to the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        a method that gets an item by keys
        """
        return self.cache_data.get(key, None)
