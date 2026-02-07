# EXERCISE 2: The Filter Generator
# Create a generator that takes a list of numbers and only yields the even ones.
# This mimics the behavior of "lazy" data processing.

def even_once(data):
    for d in data:
        if data % 2 == 0:
            yield d

numbers = [1,2,3,4,5,6,7,8,9,245,7,87,443332,23222,4,5,6,7,777,444,65,7,100]

for e in even_once(numbers):
    print(e)