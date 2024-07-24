#!/usr/bin/python3
"""
LFU Caching: Create a class LFUCache that inherits from BaseCaching
             and is a caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An LFU Cache.
    Inherits all behaviors from BaseCaching except, upon any attempt to add
    an entry to the cache when it is at max capacity (as specified by
    BaseCaching.MAX_ITEMS), it discards the least frequently used entry to
    accommodate for the new one.

    Attributes:
        __init__ - method that initializes class instance
        put - method that adds a key/value pair to cache
        get - method that retrieves a key/value pair from cache
    """

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key: str, item: str) -> None:
        """
        Add key/value pair to cache data.
        If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
        discard least frequently used entry to accommodate new entry.

        Args:
            key (str): The key for the cache entry.
            item (str): The value for the cache entry.
        """
        if key is not None and item is not None:
            if len(self.keys) >= BaseCaching.MAX_ITEMS and key not in self.keys:
                discard = self.findLFU()
                self.keys.remove(discard)
                del self.cache_data[discard]
                del self.uses[discard]
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 1
            else:
                self.keys.remove(key)
                self.keys.append(key)
                self.uses[key] += 1

    def get(self, key: str) -> str:
        """
        Return value stored in `key` key of cache.
        If key is None or does not exist in cache, return None.

        Args:
            key (str): The key for the cache entry.

        Returns:
            str: The value associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            self.uses[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self) -> str:
        """
        Return key of least frequently used item in cache.
        If multiple items have the same amount of uses, return the least
        recently used one.

        Returns:
            str: The key of the least frequently used item.
        """
        least_frequency = min(self.uses.values())
        least_frequent_keys = [k for k, v in self.uses.items() if v == least_frequency]
        for key in self.keys:
            if key in least_frequent_keys:
                return key
