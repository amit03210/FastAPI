# EXERCISE 3: Protecting Methods
# Create a class 'Website'. It should have a public method 'show_page'
# and a private method '__connect_to_db'.
# Call '__connect_to_db' inside the 'show_page' method.
# Try calling the private method from outside the class to see it fail.

from website import Website

def main():
    w1 = Website()

    print(w1.show_page())

    # print(w1.__connect_to_db())
    print(w1._Website__connect_to_db())

if __name__ == "__main__":
    main()