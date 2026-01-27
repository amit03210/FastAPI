name = "John" #String

#String formating is intsert value onto string in clean and effient way.
# Mnemonic: “C-F-F → Concatenation, Format, F-string.”

## Method 1
#Concatenation +
print("This is example of concatenation:" + "Hello " + name)

## Method 2
#using str.format(): we insert value in {} 
age = 24
print("Hello I'm {}, age is {}.".format(name, age));

## Method 3
#f-strings: f""
print(f"Hello I'm {name}, age is {age}.")



