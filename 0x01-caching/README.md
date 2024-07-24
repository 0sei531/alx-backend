# 0x01. Caching

This project involves implementing different caching algorithms in Python. Each caching system is designed to handle key-value storage with specific policies such as FIFO, LIFO, LRU, and MRU.

## Table of Contents
- [BasicCache](#basiccache)
- [FIFOCache](#fifocache)
- [LIFOCache](#lifocache)
- [LRUCache](#lrucache)
- [MRUCache](#mrucache)
- [Usage](#usage)
- [Testing](#testing)
- [Requirements](#requirements)
- [Author](#author)

## BasicCache
A basic caching system with no limit on the number of items.

### Implementation
```python
# 0-basic_cache.py
#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system without limit """
    
    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
