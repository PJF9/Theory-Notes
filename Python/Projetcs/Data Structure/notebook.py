import tree as tr

# Creating a tree object
t1 = tr.Tree()

# Filling the tree with elements
t1.insert(-1, 10)
t1.insert(0, 20, True)
t1.insert(0, 30, False)
t1.insert(1, 40, True)
t1.insert(1, 50, False)
t1.insert(2, 60, True)
t1.insert(2, 70, False)

# Remove elements by their id position
t1.pop(5)
t1.pop(6)
t1.pop(3)
t1.pop(4)

# Clear the tree
t1.clear()

# Create an new tree
t2 = tr.Tree()

t2.insert(-1, 10)
t2.insert(0, 20, True)
t2.insert(0, 30, False)
t2.insert(1, 41, True)
t2.insert(1, 42, False)
t2.insert(2, 43, True)
t2.insert(2, 44, False)

t2.insert(3, 48, True)
t2.insert(3, 47, False)
t2.insert(4, 23, True)
t2.insert(4, 34, False)

t2.insert(5, 98, True)
t2.insert(5, 77, False)
t2.insert(6, 53, True)
t2.insert(6, 14, False)

# Remove elements based on their values
# t2.remove(40, True)

# Printing the tree
print(t2, "\n")
# print(t2.print_ids())
