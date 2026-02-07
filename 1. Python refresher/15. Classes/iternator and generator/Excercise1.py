# EXERCISE 1: The Infinite Counter
# Create a generator function called 'count_up' that takes a start number.
# It should yield numbers forever (start, start+1, etc.). 
# Test it using a for loop, but use a 'break' so it doesn't run forever!

def count_up(data):
    while True:
        yield data;
        data += 1

for x in count_up(100):
    if(x == 200):
        break
    print(x)