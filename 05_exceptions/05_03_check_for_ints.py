# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:

    try:
        number = int(input("A NUMBER: "))
    except ValueError:
        print("Enter INT or be purged")
    else:
        break

# I feel like there is some wierd way I could break this that I don't know about.