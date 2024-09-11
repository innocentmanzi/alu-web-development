#!/usr/bin/python3
""" 0-main """

# Assuming BaseCaching is defined somewhere, we inherit from it
class BaseCaching:
    def __init__(self):
        """Initialize the base cache"""
        self.cache_data = {}

class BasicCache(BaseCaching):
    def __init__(self):
        """Initialize the BasicCache"""
        super().__init__()  # Call the parent class initializer

    def put(self, key, item):
        """
        Assign the item value to the key in self.cache_data.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value in self.cache_data associated with the key.
        Return None if the key is None or doesn't exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

