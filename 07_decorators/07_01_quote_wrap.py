# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quotes(init_func):
    def wrapper(text):
        output = init_func(text)
        new_string = f'"{output}"'
        print(new_string)
    return wrapper

@quotes
def hihi(text):
    return text

hihi(123)