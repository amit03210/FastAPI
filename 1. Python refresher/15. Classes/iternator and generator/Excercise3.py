# EXERCISE 3: Converting a Class to an Iterator
# Create a class 'Alphabet' that stores a string of letters.
# Implement __iter__ and __next__ so that it returns one letter at a time 
# in uppercase.

class Alphabet:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index].upper()
        self.index += 1
        return result
    

for x in Alphabet("keyboard"):
    print(x)