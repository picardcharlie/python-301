# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.
import datetime


def log_time(func):
    def wrapper():
        log_file = open("log.txt", "w")
        log_file.write(f"Executed at {datetime.datetime.now()}.")
        func()
        print(f"Completed running at {datetime.datetime.now()}.")
        log_file.close()
    return wrapper


@log_time
def loading():
    print("Loading componants")

loading()