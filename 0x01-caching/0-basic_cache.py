#!/usr/bin/python3
"""
Basic Dictionary: Create a class BasicCache that inherits from BaseCaching
                  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache.
    Inherits from class BaseCaching.

    Attributes:
        put - method that adds a key/value pair to cache
        get - method that retrieves a key/value pair from cache
    """

    def put(self, key: str, item: str) -> None:
        """
        Add key/value pair to cache.
        If either `key` or `item` is None, do nothing.

        Args:
            key (str): The key for the cache entry.
            item (str): The value for the cache entry.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Return value stored in `key` of cache.
        If key is None or does not exist in cache, return None.

        Args:
            key (str): The key for the cache entry.

        Returns:
            str: The value associated with the key, or None if
            the key is not found.

        """
        return self.cache_data.get(key, None) if key is not None else None
