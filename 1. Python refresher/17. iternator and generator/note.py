#1. Container type: is any object that hold any other objects. like list, sets, dict, str.

#2. Container type we can use 'in' operator to test the membership.
"a" in ["a", "b", "c"]   # True
2 in {1, 2, 3}           # True

#3. Collection is broader term, means any data structure that group multiple elements together. Like list, sets, generator, iterator, etc.

#4 iterator or generator are collections but not container since they can't do membership test (in) directly to them.

#5. Iterator is the mechanism that allows us to traverse those elements one by one, It doesn’t matter if the source is a container (with stored elements) or a collection that generates them on the fly. The iterator protocol (__iter__ and __next__) unifies the process.


