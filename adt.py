class SetADT:
    def __init__(self):
        self.elements = []

    def add(self, new_element):
        """Adds an element to the set (if not already present)."""
        if new_element not in self.elements:
            self.elements.append(new_element)

    def remove(self, element):
        """Removes an element from the set (if present)."""
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        """Checks if an element exists in the set."""
        return element in self.elements

    def size(self):
        """Returns the number of elements in the set."""
        return len(self.elements)

    def iterator(self):
        """Returns an iterator over the set elements."""
        return iter(self.elements)

    def intersection(self, other_set):
        """Returns a new set containing common elements of both sets."""
        result = SetADT()
        for element in self.elements:
            if other_set.contains(element):
                result.add(element)
        return result

    def union(self, other_set):
        """Returns a new set containing all elements from both sets."""
        result = SetADT()
        for element in self.elements:
            result.add(element)
        for element in other_set.elements:
            result.add(element)
        return result

    def difference(self, other_set):
        """Returns a new set with elements in this set but not in the other."""
        result = SetADT()
        for element in self.elements:
            if not other_set.contains(element):
                result.add(element)
        return result

    def is_subset(self, other_set):
        """Checks if the current set is a subset of another set."""
        for element in self.elements:
            if not other_set.contains(element):
                return False
        return True

    def display(self):
        """Displays the set elements."""
        print("{", ", ".join(map(str, self.elements)), "}")


# Example Usage
set1 = SetADT()
set2 = SetADT()

set1.add(1)
set1.add(2)
set1.add(3)

set2.add(3)
set2.add(4)
set2.add(5)

print("Set 1:", end=" ") 
set1.display()
print("Set 2:", end=" ")
set2.display()

# Operations
print("\n🔹 Intersection:", end=" ")
set1.intersection(set2).display()

print("🔹 Union:", end=" ")
set1.union(set2).display()

print("🔹 Difference (Set1 - Set2):", end=" ")
set1.difference(set2).display()

print("🔹 Is Set1 a subset of Set2?:", set1.is_subset(set2))