# ================================
# 📝 Python Dictionary Practice Sheet (Blank)
# ================================

# -------------------------------
# Level 1: Basics
# -------------------------------

# 1. Create a dictionary of 3 fruits and their colors.
# Print the color of "banana".
# Add a new fruit "orange".
# Delete "grapes".
fruits = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
print(fruits)
fruits['grapes'] = 'green'
print(fruits)
del fruits['grapes']
print(fruits)

# 2. Convert list of tuples into dictionary:
data = [("name", "Alice"), ("age", 25), ("city", "Lucknow")]
# TODO: Make dictionary from data
# TODO: Print the city value
students = dict(data)
print(students)
print(students['city'])

# -------------------------------
# Level 2: Iteration & Methods
# -------------------------------

scores = {"math": 90, "science": 85, "english": 88}
# TODO: Print all keys
# TODO: Print all values
# TODO: Print all key-value pairs
# TODO: Loop through dictionary and print subject → score

for k in scores:
    print(k)

print(scores.keys())
print(scores.values())

for k,v in scores.items():
    print(k, v)

for k,v in scores.items():
    print(k + " -> " + str(v))


# -------------------------------
# Level 3: Updating & Checking
# -------------------------------

student = {"name": "Bob", "age": 20}

# TODO: Update age to 21
# TODO: Add grade "A"
# TODO: Check if "name" exists
# TODO: Safely get "city"

student['age'] = 21;
student['grade'] = "A"
print('name' in student)
print(student.get('city'))
print(student)

# -------------------------------
# Level 4: Nested Dictionaries
# -------------------------------

students = {
    "s1": {"name": "Alice", "marks": 85},
    "s2": {"name": "Bob", "marks": 90}
}

# TODO: Print Bob’s marks
# TODO: Add new student s3
# TODO: Increase Alice’s marks by 5
print(students['s2']['marks'])
students['s3'] = {"name": 'Charlie', "marks": 95}
students['s1']['marks'] = students['s1']['marks'] + 5
print(students)

# -------------------------------
# Level 5: Applications
# -------------------------------

text = "apple banana apple orange banana apple"
# TODO: Count word frequency using dictionary
word_freq = {}
text_word = text.split(' ')

for word in text_word:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] = word_freq[word]+1

# for word in text_word:
#   word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)

phonebook = {"Alice": 1234, "Bob": 5678, "Charlie": 9999}
# TODO: Find name with phone number 5678
for k, v in phonebook.items():
    if v == 5678:
        print(k)

result = [k for k, v in phonebook.items() if v == 5678]
print(result)

# -------------------------------
# Challenge Exercise
# -------------------------------

keys = ["name", "age", "city"]
values = ["David", 30, "Delhi"]

# TODO: Combine into dictionary using zip
info = {}
for k, v in zip(keys, values):
    info[k] = v
print(info)

info2 = dict(zip(keys, values))
print(info2)

info3 = {k:v for k, v in zip(keys, values)}
print(info3)
