#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) | Depends on the length of buckets"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) | Depends on the quantity of keys"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) | Depends on the number of items"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) | Depends on the number of entries"""
        count = 0
        for bucket in self.buckets:
            count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) if bucket contains only one entry
        Running time: O(n) if bucket contains multiple entries"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        found = bucket.find(lambda item: item[0] == key)
        return bool(found)



    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        found = bucket.find(lambda item: item[0] == key)
        if found is not None:
            return found[1]
        raise KeyError("Key not longer exists in this hash table")

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) when finding index and appending
        Running time: O(l) when searching for item within bucket
        l is length -> O(l) + O(1) = O(l)
        """
        index = self._bucket_index(key)  # O(1) time
        # Get bucket specified by key from list
        bucket = self.buckets[index]  # O(1) time
        # Check if bucket exists to add or replace
        if self.contains(key): # O(l) time for l items in list
            bucket.delete(key) # O(l) length of the list
        bucket.append((key, value)) # O(1) time


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        found = bucket.find(lambda item: item[0] == key) # O(n)
        if found is not None:
            bucket.delete(found)
            return
        else:
            raise KeyError("Key not longer exists in this hash table")

def test_hash_table():
    ht = HashTable()
    ht.set("Johnathan", 9000)
    ht.set("Jessica", "likes candy")

    if ht.contains("Johnathan"):
        print("ht contains 'Johnathan': True")

    ht.delete("Johnathan")

    print('hash table: {}'.format(ht))
    # print('all keys: {}'.format(ht.keys()))
    # print('all values: {}'.format(ht.values()))
    # print('all items: {}'.format(ht.items()))
    # print('length: {}'.format(ht.length()))

    # print('\nTesting set:')
    # for key, value in [('I', 1), ('V', 5), ('X', 10)]:
    #     print('set({!r}, {!r})'.format(key, value))
    #     ht.set(key, value)
    #     print('hash table: {}'.format(ht))
    #
    # print('\nTesting get:')
    # for key in ['I', 'V', 'X']:
    #     value = ht.get(key)
    #     print('get({!r}): {!r}'.format(key, value))

    # print('contains({!r}): {}'.format('X', ht.contains('X')))


    # Enable this after implementing delete method
    # delete_implemented = False
    # if delete_implemented:
    #     print('\nTesting delete:')
    #     for key in ['I', 'V', 'X']:
    #         print('delete({!r})'.format(key))
    #         ht.delete(key)
    #         print('hash table: {}'.format(ht))
    #
    #     print('contains(X): {}'.format(ht.contains('X')))
    #     print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
