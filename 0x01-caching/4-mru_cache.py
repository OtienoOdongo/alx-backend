#!/usr/bin/python3
"""
MRU cache placement
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Most Recently Used (MRU) caching system """

    def __init__(self):
        """ Initialize the MRU Cache """
        self.mru_stack = []
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using the MRU strategy """
        if key and item:
            if self.cache_data.get(key):
                self.mru_stack.remove(key)
            while len(self.mru_stack) >= self.MAX_ITEMS:
                deleted_key = self.mru_stack.pop()
                self.cache_data.pop(deleted_key)
                print(f'DISCARD: {deleted_key}')
            self.mru_stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve a cached item by its key """
        if self.cache_data.get(key):
            self.mru_stack.remove(key)
            self.mru_stack.append(key)
        return self.cache_data.get(key)
