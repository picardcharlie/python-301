# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def censor(init_function):
    def wrapper(words):
        check_text = init_function(words)
        check_text_list = check_text.split()
        censored = ["shoot", "turd", "catpoop", "lampshade"] #all the banned words in my house

        for x in range(len(check_text_list)):

            #Looks through the censored words.  Leaves the first letter of the word and stars out the rest of it.
            if check_text_list[x] in censored:
                check_text_list[x] = check_text_list[x][:1] + ("*" * (len(check_text_list[x]) - 1))

        new_text = " ".join(check_text_list)
        print(new_text)

    return wrapper

@censor
def teexxtt(words):
    return words

teexxtt("I like to shoot catpoop onto my lampshade .")

# I'm going to have to get into regular expressions if I want it to censor the last word.
# Python considers the punctuation as part of the word.