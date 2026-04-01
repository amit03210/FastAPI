#1. Container type: is any object that hold any other objects. like list, sets, dict, str.

#2. Container type we can use 'in' operator to test the membership.
"a" in ["a", "b", "c"]   # True
2 in {1, 2, 3}           # True

#3. Collection is broader term, means any data structure that group multiple elements together. Like list, sets, generator, iterator, etc.

#4 iterator or generator are collections but not container since they can't do membership test (in) directly to them.

#5. Iterator is the mechanism that allows us to traverse those elements one by one, It doesn’t matter if the source is a container (with stored elements) or a collection that generates them on the fly. The iterator protocol (__iter__ and __next__) unifies the process.


#6. protocol: “A set of rules (special methods) that an object must follow to behave in a certain way.”
# A Python object is considered an iterator when it implements two special methods collectively known as the iterator protocol. 
# .__iter__()	Called to initialize the iterator. It must return an iterator object.
# .__next__()	Called to iterate over the iterator. It must return the next value in the data stream.
