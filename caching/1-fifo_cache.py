#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

class BaseCaching:
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the base cache"""
        self.cache_data = {}

class FIFOCache(BaseCaching):
    def __init__(self):
        """Initialize the FIFOCache"""
        super().__init__()  # Call the parent class initializer
        self.order = []  # List to keep track of the order of keys (for FIFO)

    def put(self, key, item):
        """
        Add an item to the cache, following FIFO principle.
        If key or item is None, do nothing.
        If the cache exceeds MAX_ITEMS, discard the first added item.
        """
        if key is None or item is None:
            return

        # If key already exists, update the value but maintain its order in FIFO
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # FIFO: Remove the oldest item
                first_key = self.order.pop(0)  # Get and remove the first item in the order list
                del self.cache_data[first_key]  # Remove from cache_data
                print(f"DISCARD: {first_key}")

            # Add the new key to the cache and track its order
            self.cache_data[key] = item
            self.order.append(key)  # Append the new key to the order list

    def get(self, key):
        """
        Retrieve the value linked to key in the cache.
        If key is None or doesn't exist, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

