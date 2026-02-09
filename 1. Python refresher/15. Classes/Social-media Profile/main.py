# EXERCISE 3: The Social Media Profile
# Create a Profile class. Use __init__ to set a username and a list of 'posts'.
# Add a method 'add_post' that appends a string to the posts list.
# Ensure that adding a post to one user doesn't add it to another!

from profile import Profile

def main():
    user1 = Profile('Jonny')
    user2 = Profile('Alice')
    user3 = Profile('Claudia')

    user1.add_post("I prefer Gamrix' two-step version.")
    user1.add_post("Note the additional pair of braces needed for nesting.")
    user1.add_post("I don't understand, it seems to do exactly what you want.")

    user2.add_post("Find the answer to your question by asking.")

    print(user1)
    print(user2)
    print(user3)

if __name__ == "__main__":
    main()