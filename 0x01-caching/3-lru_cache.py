#!/usr/bin/python3
"""
LRU cache placement
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Custom implementation of an LRUCache """

    def __init__(self):
        """ Initialize the custom LRUCache """
        super().__init__()
        self.custom_queue = []

    def put(self, key, item):
        """ Store the item in the cache """
        if key and item:
            if self.cache_data.get(key):
                self.custom_queue.remove(key)
            self.custom_queue.append(key)
            self.cache_data[key] = item
            if len(self.custom_queue) > self.MAX_ITEMS:
                discard_key = self.custom_queue.pop(0)
                self.cache_data.pop(discard_key)
                print(f'DISCARD: {discard_key}')

    def get(self, key):
        """ Retrieve the value associated with the given key """
        if self.cache_data.get(key):
            self.custom_queue.remove(key)
            self.custom_queue.append(key)
        return self.cache_data.get(key)
