# EXERCISE 5: The "Countdown" Iterator
# Create a class-based iterator that takes a number and counts down to 0.
# When it hits 0, it should raise StopIteration.
# Compare this to a generator function doing the same thing—which is easier?

#iterator class
class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.data >= -1:
            raise StopIteration
        result = self.data
        self.data -= 1
        return result
    
for d in Reverse(100):
    print(d) 

print("----------------------")

#generator
def count_down(n):
    while n>=0:
        yield n
        n -= 1

for x in count_down(13):
    print(x)