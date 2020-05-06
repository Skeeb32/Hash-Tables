class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        # self.prime = 1099511628211
        # self.offset = 14695981039346656037
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        # hash_bytes = key.encode()
        # total = self.offset
        # for b in hash_bytes:
        #     total *= self.prime
        #     total ^= b
        #     total &= 0xffffffffffffffff
        # return total
        # The FNV_offset_basis is 
        # the 64-bit FNV offset basis value: 
        # 14695981039346656037 (in hex, 0xcbf29ce484222325)
        # Exclusive OR Operator (^=)
        h = 14695981039346656037
        for b in str(key).encode():
            h *= 1099511628211
            h ^= b
            h &= 0xffffffffffffffff
        return h


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity
        

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Add new entry
        newEntry = HashTableEntry(key, value)
        # has the key and find its index
        newIndex = self.hash_index(key)
        # check if newindex has empty storage
        if self.storage[newIndex] is None:
            self.storage[newIndex] = newEntry
            return
            # get the indext storage
        node = self.storage[newIndex]
         # store the value in the newIndex
        prev = None
        while node is not None: #Iterate through Node till you reach None
            # print(node.key, node.value, value)
            if node.key == key:
                # print(value)
                node.value = newEntry.value
                # print("Hello", node.key, node.value, value)
                return
                # go to next node
            prev = node
            node = node.next

        prev.next = newEntry
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        val = self.get(key)
        if val == None:
            print("Not found")
        if val != None:
            hash_index = self.hash_index(key)
            node = self.storage[hash_index]
            prev = None
            while node is not None:
                if node.key == key:
                    if prev != None:
                        prev.next = None
                    else:
                        self.storage[hash_index] = node.next
                prev = node
                node = node.next

        # index = self.hash_index(key)
        # self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None
         

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # Step 1: Make a new, bigger table/array
        # Step 2: Go through all the old elements, and hash into the new list
        # Rule of thumb:
        # If you resize bigger, double size if smaller halve the size.
        new_capacity = self.storage
        if self.storage > 0.7:
            self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        self.storage = new_array
        for element in new_capacity:
            if element is not None:
                self.put(element.key, element.value)
                element = element.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
