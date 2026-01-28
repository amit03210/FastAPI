"""
Sets: Unique and unordered collection.
Syntax: {} or set() function.
Tip to remember {} Scrambled Curly as unordered and basket for no duplicates

Properties:
1. No duplicates allowed.
2. Unordered (no indexing).
3. Useful for membership tests and removing duplicates.
"""
numbers = {1,3,5,5} # 1,3,5
print(numbers)

# Set operations
# 1. Addition
numbers.add(6)
print(numbers)

# 2. Remove
numbers.remove(6)
print(numbers)

a = {3,4}
b = {4,5}

# 3. Union |
print(a | b)

# 4. Common item or interaction &
print(a&b)

# 5. Present in one, but not another or difference -
print(a-b)

"""
Real life anology
Set = Guest List: Each guest’s name appears only once, order doesn’t matter.
Union = Two guest lists combined.
Intersection = Guests common to both lists.
Difference = Guests invited by one host but not the other.
"""

#============================================================================
"""
Tuples: ordered and immutable collection
Syntax: () 
Tip to remember: Like GPS coordinates (27.5, 78.6) → fixed, ordered.
() => Tidy Parentheses: ordered, fixed.

Properties: 
1. Ordered => index based
2. Immutable => cannot be changed
3. Can contain mix types
4. Can contain duplicates
"""
coordinates = (10, 20, 65,70,-9)

#indexing
print(coordinates[0])

#slicing
print(coordinates[1:3])

"""
Real life analogy:
1. Train Carriage: Each carriage has a fixed position and cannot be rearranged.
2. Birth Certificate: Once created, details cannot be changed.
"""

print("==============Excercise from here===================")

# 1. Exercise: Create a set of 5 numbers with duplicates. 
# Print the set and observe how duplicates are removed.
# Expected Output:
# {1, 2, 3, 4, 5}
numbers = {1,1,4,4,7}
print(numbers)

"""
2. Given two sets:
Perform and print:
Union
Intersection
Difference (a - b)
Symmetric Difference (a ^ b)
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

# 3. Create a set of fruits. Ask the user for a fruit name and check if it’s in the set.
# Example:
# Input: "apple"
# Output: apple is in the set!
fruits = {'apple', 'banana', 'chickoo', 'orange'}
if 'apple' in fruits:
    print('apple is in the set')

"""
4. Create a tuple of 4 colors. Print:
The first color
The last color
A slice of the first 3 colors
"""
colors = ('red', 'red', 'blue', 'orange')
print(colors[0])
print(colors[-1])
print(colors[0:3])

# 5. Try to change one element of a tuple and see what error occurs.
colors = ("red", "blue", "green")
# colors[1] = "yellow"   # should raise TypeError

#6. Create a tuple of sets and a set of tuples.
# Print both and explain the difference.
tuple_of_sets = ({1, 2}, {3, 4}, {1,2}, {1,3})
set_of_tuples = {(1, 2), (3, 4), (1,2), (1,3)}
print(tuple_of_sets)
print(set_of_tuples)

"""
7. Write a program that:

Stores student names in a tuple (fixed list).
Stores their marks in a set (no duplicates).
Prints the highest and lowest marks.
"""
student = ('amit', 'rahul', 'neha', 'aditya')
marks = {12,32,13,50}
listMarks = list(marks)
listMarks.sort()
print(f"Highest marks is {listMarks[-1]} and lowest marks is {listMarks[0]}")
#or
#print(f"Highest marks is {max(marks)} and lowest marks is {min(marks)}")
