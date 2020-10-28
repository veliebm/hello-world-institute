"""
This file defines a class called a Trie to use for autocomplete.py

Created 9/18/2020 by Ben Velie.
veliebm@gmail.com

"""


class Trie:
    """
    Stores data in a very tree-like fashion :)

    """

    def __init__(self, value, count=1, children=set()):

        self.value = value
        self.count = count
        self.parent = None

        for child in children:
            assert isinstance(child, Trie), "Child isn't a Trie."

        self.children = set()


    def __contains__(self, value):
        child_values = {child.value for child in self}
        return value in child_values


    def __repr__(self):

        child_values = {child.value for child in self}

        return f"Trie({self.value}, {self.count}, {self.children})"


    def __getitem__(self, value):
        for trie in self.children:
            if trie.value == value:
                return trie

        raise KeyError(f"Child with value '{value}' doesn't exist")


    def __iter__(self):
        for child in self.children:
            yield child


    def __len__(self):
        return len(self.children)


    def add(self, value):
        """
        Creates/returns a child trie for the target value. If it already exists, returns trie for target value.

        Increments count of child by one.

        """

        try:
            self[value].count += 1
            return self[value]
        
        except KeyError:
            new_child = Trie(value)
            new_child.parent = self
            self.children.add(new_child)
            return new_child


    def store(self, iterable):
        """
        Stores iterable into a bunch of sub-tries.

        """
        
        if len(iterable) > 0:
            subtrie = self.add(iterable[0])
            return subtrie.store(iterable[1:])
        else:
            return self