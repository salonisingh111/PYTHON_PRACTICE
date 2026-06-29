class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        # Use sum() and ord() to calculate the hash
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            # Optional: Clean up empty dictionary
            if not self.collection[hash_key]:
                del self.collection[hash_key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            return self.collection[hash_key].get(key)
        return None