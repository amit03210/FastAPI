# Exercise 1: Ask user for two numbers and print their sum with proper formatting

# print("Enter two number")
# x = int(input("Number 1: "))
# y = int(input("Number 2: "))
# print("Sum of both number is:", x+y);

# Exercise 2: Print a table of numbers (1–10) with aligned columns
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}", end="\n")
    print("----------------")


# Exercise 3: Take a name and age as input and display a formatted sentence

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello, {1}, you are {0} year old.".format(age, name))

# Exercise 4: Show difference between str() and repr() using a list
fruits = "apple\nbanana\norange"
print(str(fruits))
print(repr(fruits))

# Exercise 5: Write user input into a file and read it back

# feedback = input("Enter your Feedback: ")
# f = open("1. Python refresher\\13. Input-Output Adv\\Story.txt", "w")
# f.write(feedback)
# f.close()

# Exercise 6: Format a floating-point number as currency
n = 1254.255463
print("${:.2f}".format(n))

# Exercise 7: Log multiple lines into a file using with
with open("1. Python refresher\\13. Input-Output Adv\\Story_2.txt") as f:
    print(f.readlines())

# Exercise 8: Read a file line by line and print line numbers
with open("1. Python refresher\\13. Input-Output Adv\\Story_2.txt") as f:
    lines = f.readlines()
    for l in range(len(lines)):
        print(f"{l+1}. {lines[l].strip()}")

# Exercise 9: Build a simple CLI greeting that loops until user types 'exit'
inn = input("Enter your name (or type 'exit' to quit): ")

while inn != "exit":
    print(f"Hello, {inn}!")   # greet the user
    inn = input("Enter your name (or type 'exit' to quit): ")

# Exercise 10: Capture errors when converting input to int and print a message

try:
    bdate = int(input("What is your birthdate: \n"))
    print("Got it, thank your your input.")
except ValueError:
    print("OOps you are trying to input string, we asked your birthdate.")