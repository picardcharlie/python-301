# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(init_func):
    def wrapper(text, char):
        # x25 should do.
        print(char * 25)
        print(text)
        print(char * 25)

    return wrapper


@decorate
def textinput(text, char):
    return text, char

textinput("I need a nap", "&")