class Node:
    #Node class to represent a key value pair in the hash table
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    #Hash Table class with chaining.
    def __init__(self, size):
        #Initializing the hash table with a given size.
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        #Hash function to map keys to indices
        return hash(key) % self.size

    def insert(self, key, value):
        #Here Inserting a key value pair into the hash table.
        index = self._hash_function(key)
        if self.table[index] is None:
            # If the index is empty, create a new node
            self.table[index] = Node(key, value)
        else:
            # If the index is not empty, traverse the linked list and append the new node
            node = self.table[index]
            while node.next:
                if node.key == key:
                    # If the key already exists, update the value
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                # If the key already exists, update the value
                node.value = value
            else:
                # Append the new node to the linked list
                node.next = Node(key, value)

    def search(self, key):
        """Retrieve the value associated with a given key."""
        index = self._hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash_function(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    # Remove the node from the linked list
                    prev.next = node.next
                else:
                    # Remove the first node in the linked list
                    self.table[index] = node.next
                return
            prev = node
            node = node.next

# Example usage:
hash_table = HashTable(10)
hash_table.insert('Kiwi', 5)
hash_table.insert('pineapple', 7)
hash_table.insert('Grapes', 3)

print(hash_table.search('Kiwi'))  # Output: 5
print(hash_table.search('Pineapple'))  # Output: 7
print(hash_table.search('Grapes'))  # Output: 3

hash_table.delete('Pineapple')
print(hash_table.search('Pineapple'))  # Output: None
