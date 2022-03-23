import random
import string


class Node:
    '''Structure for a single key-value pair.'''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyDict:
    '''
    My implementation of a hash table.
    An analogue of Python dictionary.
    '''

    def __init__(self, capacity=32, debug=False):
        self.capacity = capacity
        self.debug = debug
        self.size = 0
        self.taken = 0
        self.__buckets = [None] * self.capacity

    def __setitem__(self, key, value):
        '''
        Overload of __setitem__() method.
        Called by: obj[key] = value.
        '''
        # Check load, rehash if >= 0.75
        self.rehash()

        self.size += 1
        index = hash(key) % self.capacity
        node = self.__buckets[index]

        # No collision: put node in empty bucket
        if node is None:
            self.__buckets[index] = Node(key, value)
            self.taken += 1
            return

        # Collision: iterate bucket, put node at end
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def __getitem__(self, key):
        '''
        Overload of __getitem__() method.
        Called by: obj[key]
        '''
        index = hash(key) % self.capacity
        node = self.__buckets[index]

        # Iterate bucket until key is found
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value

    def __str__(self):
        '''
        Overload of __str__() method.
        Called by: str(obj).
        '''
        pairs = list()
        for bucket in self.__buckets:
            node = bucket
            while node is not None:
                k = node.key
                v = node.value
                k = f"\'{k}\'" if type(k) is str else k
                v = f"\'{v}\'" if type(v) is str else v
                pairs.append(f"{k}: {v}")
                node = node.next
        return f"\u007b{', '.join(pairs)}\u007d"

    def __len__(self):
        '''
        Overload of __len__() method.
        Called by len(obj).
        '''
        return self.size

    def __iter__(self):
        '''
        Overload of __iter__() method.
        Returns iterator object.
        '''
        self.index = 0
        self.node = self.__buckets[self.index]
        return self

    def __next__(self):
        '''
        Overload of __next__() method.
        Returns next item in sequence.
        '''
        # Finding next filled bucket
        while self.node is None:
            self.index += 1
            if self.index >= self.capacity:
                raise StopIteration
            self.node = self.__buckets[self.index]

        # Getting key-value pair and going to next node
        k, v = self.node.key, self.node.value
        self.node = self.node.next
        return k, v

    def rehash(self):
        '''
        Rehashing method.
        Doubles capacity and readds items to buckets.
        '''
        # Rehashing is only needed if 75% or more of buckets are filled
        if self.taken / self.capacity < 0.75:
            return

        # Create new counters and set of buckets
        newcapacity = self.capacity * 2
        newsize = 0
        newtaken = 0
        newbuckets = [None] * newcapacity

        # Debug print, can be omitted
        if self.debug:
            print(f"Rehashing. Capacity {self.capacity} -> {newcapacity}")

        # Add all items to new buckets
        for key, value in self:
            newsize += 1
            index = hash(key) % newcapacity
            node = newbuckets[index]

            # No collision: put node in empty bucket
            if node is None:
                newbuckets[index] = Node(key, value)
                newtaken += 1
                continue

            # Collision: iterate bucket, put node at end
            prev = node
            while node is not None:
                prev = node
                node = node.next
            prev.next = Node(key, value)

        # Debug print, can be omitted
        if self.debug:
            oldload = self.taken / self.capacity
            newload = newtaken / newcapacity
            print(f"Rehashing done. Load {oldload:.3f} -> {newload:.3f}")

        # Replacing old counters and bucket set with new ones
        self.__buckets = newbuckets
        self.capacity = newcapacity
        self.size = newsize
        self.taken = newtaken


def test(n=32):
    # Comparing to dictionary
    assert n > 0, 'Number of pairs must be positive'
    letters = string.ascii_letters
    a = MyDict()
    b = dict()
    c = list()

    for _ in range(n):
        key = ''.join(random.choice(letters) for _ in range(8))
        value = random.randrange(8096)
        a[key] = value
        b[key] = value
        if random.randrange(8) == 0:
            c.append(key)

    for key in c:
        print(f"MyDict:\ta['{key}'] = {a[key]}")
        print(f"dict:\tb['{key}'] = {b[key]}")
        print(f"The values are{' ' if a[key] == b[key] else ' not '}equal")


def main():
    # Demonstration of writing, reading, types
    a = MyDict()
    a[1] = 1983
    a[2] = '1984'
    a['3'] = 1986
    a['1988'] = 'ajfa'
    a['black'] = 'black', 1991
    a[(96, 97)] = 'load', 'reload'
    a[0.99] = 'S', 'M'

    print(f"a[1] contains {a[1]} ({type(a[1])})")
    print(f"a[2] contains {a[2]} ({type(a[2])})")
    print(f"a['1988'] contains {a['1988']} ({type(a['1988'])})")
    print("Entire dictionary:")
    print(a)

    # Demostration of rehashing and size flexibility
    b = MyDict(8, debug=True)
    for i in range(1025):
        b[i] = f'str_{i}'
    for i in range(11):
        print(f'b[{2 ** i}] = {b[2 ** i]}')
    if b['no such key'] is not None:
        print(f"Element 'no such key': {b['no such key']} found... somehow")
    else:
        print(f"Getting a non-existing element returned {b['no such key']}")


if __name__ == '__main__':
    main()
    test()
