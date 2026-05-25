class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, key_str):
        return sum(ord(char) for char in key_str)
    
    def add(self, key, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value
    
    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
        
    def lookup(self, key):
        hashed = self.hash(key)
        print(hashed)

        if hashed not in self.collection or key not in self.collection[hashed]:
            return None
        else:
            return self.collection[hashed][key]

def test():
    print("--- Initializing Hash Table ---")
    ht = HashTable()

    # 1. Test adding and looking up items
    print("\n1. Testing Add and Lookup:")
    ht.add("apple", "red")
    ht.add("banana", "yellow")
    
    print(f"Lookup 'apple': {ht.lookup('apple')} (Expected: 'red')")
    print(f"Lookup 'banana': {ht.lookup('banana')} (Expected: 'yellow')")

    # 2. Test looking up a non-existent key
    print("\n2. Testing Missing Key Lookup:")
    print(f"Lookup 'grape': {ht.lookup('grape')} (Expected: None)")

    # 3. Test updating an existing key
    print("\n3. Testing Updating a Key:")
    ht.add("apple", "green")
    print(f"Lookup updated 'apple': {ht.lookup('apple')} (Expected: 'green')")

    # 4. Test Hash Collision
    # "silent" and "listen" have the exact same characters, so they will generate the same hash value.
    print("\n4. Testing Hash Collision Handling:")
    print(f"Hash of 'silent': {ht.hash('silent')}")
    print(f"Hash of 'listen': {ht.hash('listen')}")
    
    ht.add("silent", "quiet")
    ht.add("listen", "hear")

    print(f"Lookup 'silent': {ht.lookup('silent')} (Expected: 'quiet')")
    print(f"Lookup 'listen': {ht.lookup('listen')} (Expected: 'hear')")
    
    # Verify both exist under the same hash bucket in the underlying collection
    hashed_val = ht.hash("silent")
    print(f"Underlying bucket storage: {ht.collection[hashed_val]}")

    # 5. Test removing an item
    print("\n5. Testing Remove:")
    ht.remove("banana")
    print(f"Lookup 'banana' after removal: {ht.lookup('banana')} (Expected: None)")

    # 6. Test removing one item from a collided hash bucket
    print("\n6. Testing Remove with Collision:")
    ht.remove("silent")
    print(f"Lookup 'silent' (removed): {ht.lookup('silent')} (Expected: None)")
    print(f"Lookup 'listen' (should still exist): {ht.lookup('listen')} (Expected: 'hear')")


if __name__ == "__main__":
    test()