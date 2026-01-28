"""
- *name → collects extra positional arguments into a tuple.
- **name → collects extra keyword arguments into a dictionary.
You can use both together, but *name must come before **name.

*args → “Grab all the extra values into a tuple.”
**kwargs → “Grab all the extra named values into a dictionary.”
"""

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")