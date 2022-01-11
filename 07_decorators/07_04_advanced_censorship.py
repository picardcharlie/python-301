# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def words(*args):
    def censor(init_func):
        def wrapper(sentence):
            text_input = init_func(sentence).split()
            #starts cycling through the censored words.
            for censor_word in args:
                # check to see if the word is inside the text list.
                for x in range(len(text_input)):
                    if censor_word in text_input[x]:
                        text_input[x] = text_input[x][:1] + ("*" * (len(text_input[x]) - 1))

            output_text = " ".join(text_input)
            print(output_text)
        return wrapper
    return censor


@words("cold", "tired", "homework")
def text_(sentence):
    return sentence

text_("It's so cold out and I'm tired, yet restless while trying to do this homework but I'm not working so ok")