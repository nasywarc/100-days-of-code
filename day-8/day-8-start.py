# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("This")
    print("Is")
    print("Function")


def greet_with_name(name):
    print(f"Hello {name}")


def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"Do you come from {location}?")


# greet()
# greet_with_name("Jack")

# positional arguments
# greet_with_name_location("Jack", "England")

# keywords arguments
greet_with_name_location(location="England", name="Jack")
