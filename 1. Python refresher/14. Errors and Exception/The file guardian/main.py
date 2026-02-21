# EXERCISE 3: The File Guardian
# Attempt to open a file named 'secrets.txt' in read mode.
# Catch the FileNotFoundError and print a friendly message.
# Use the 'finally' block to print "Execution Finished".

try:
    f = open('secrets.txt', '+r')
    print(f.readline())
except FileNotFoundError:
    print("File not exist sir.")
finally:
    print("Execution finished")