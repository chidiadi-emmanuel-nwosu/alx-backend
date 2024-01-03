#!/usr/bin/env python3
""" LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ a caching system class that inherits from
        BaseCaching
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = next(iter(self.cache_data))
                del self.cache_data[discard_key]
                print('DISCARD:', discard_key)

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        item = self.cache_data.get(key) or None
        if item:
            del self.cache_data[key]
            self.cache_data[key] = item
        return item
