#!/usr/bin/env python3
""" LFUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ a caching system class that inherits from
        BaseCaching
    """
    def __init__(self):
        """ Initialise
        """
        super().__init__()
        self.lfu_tracker = {}

    def evict_key(self):
        """ Removes the least frequently used key
        """
        min_value = min(self.lfu_tracker.values())
        min_keys = [key for key, value in self.lfu_tracker.items()
                    if value == min_value]
        for key in self.cache_data:
            if key in min_keys:
                del self.cache_data[key]
                del self.lfu_tracker[key]
                return key
        return None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = self.evict_key()
                print('DISCARD:', discard_key)

            self.cache_data[key] = item

            if key in self.lfu_tracker:
                self.lfu_tracker[key] += 1
            else:
                self.lfu_tracker[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.lfu_tracker[key] += 1
            return self.cache_data[key]
        return None
