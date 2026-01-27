""" 
List is python data structure to save data
Properties:
1. Ordered: index based.
2. Mutable: Can add, remove, delete, modify.
3. Allow duplicates: same value can be stored.
4. Allow multiple data types in same list.
"""
#it is okay according to list.
phoneNumber = [365412, "91 - 9106857654", 91.65528545]
print(phoneNumber)

fruits = ['Apple', 'Mango', 'Banana', 'Orange', 'Jackfruit']
print(fruits)
print(fruits[1])
print(fruits[-1])

#slicing
#show fruits item from index 0 to 3, note last item is not included from slice
print(fruits[0:4]) 

#Useful method of lists
#1. append(value): adds value to the end of list
fruits.append('Chickoo')
print(fruits)

#2. insert(pos, val): add value to the desired position
fruits.insert(1, "Apple")
print(fruits)

#3. remove(val): remove 1st item matching with input value
fruits.remove("Apple")
print(fruits)

#4. pop(pos): remove the last item of the list if pos not given
print(fruits.pop())
print(fruits)

# Other useful methods
print(len(fruits)) #5. length of list
fruits.sort() #6. Sort the list in ascending order
print(fruits)
fruits.reverse() #7. Sort the list in descending order
print(fruits)
fruits.clear() #8. remove all item from the list
print(fruits)

"""
# Best Practices
- Use lists when order matters.
- For large numeric datasets, prefer arrays (NumPy).
- Keep lists consistent (avoid mixing too many types).
"""

# Excercise:
print("============Execercise from here=================")
#1. Create a list of 5 fruits and print the first and last fruit.
# Expected Output:
# First fruit: apple
# Last fruit: mango
fruits = ['Apple', 'Mango', 'Banana', 'Orange', 'Jackfruit']
print(fruits)
print(fruits[1])
print(fruits[-1])

#2. Make a list of 10 numbers. Print:
"""
The 3rd number
The last number
The first 5 numbers using slicing
"""
# Example Output:
# 3rd number: 3
# Last number: 10
# First 5 numbers: [1, 2, 3, 4, 5]
numbers = [1,2,3,4,5,6,7,8,9,10]
print("The 3rd number is {}".format(numbers[2]))
print("The Last number is {}".format(numbers[-1]))
print("The First 5 numbers:  {}".format(numbers[0:5]))


#3. Start with a list: colors = ["red", "blue", "green"]
"""
Change "blue" to "yellow"
Add "purple" at the end
Remove "red"
"""
# Expected Output:
# ["yellow", "green", "purple"]
colors = ["red", "blue", "green"]
colors[1] = "yellow"
colors.append("purple")
colors.remove('red')
print(f"{colors}")

#4. Create a list of numbers: [5, 2, 9, 1]
"""
Find the length of the list
Sort the list
Reverse the list
"""
# Expected Output:
# Length: 4
# Sorted: [1, 2, 5, 9]
# Reversed: [9, 5, 2, 1]
numbers = [5, 2, 9, 1]
print(len(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#5. Create a list of students with their marks:
# students = [["Alice", 85], ["Bob", 90], ["Charlie", 78]]
# Print Bob’s marks.
# Expected Output:
# 90
students = [["Alice", 85], ["Bob", 90], ["Charlie", 78]]
print(students[1][1])

# Write a program that:
"""
Stores 5 numbers in a list.
Calculates the sum and average.
"""
# Example Output:
# Sum = 50
# Average = 10.0
numberList = [433,553,22,78,-24]
sum = 0
for x in numberList:
    sum += x;
print("Sum is: " + str(sum))
print("Average is: " + str(sum/len(numberList)))
print(numberList.pop(2))
print(numberList)