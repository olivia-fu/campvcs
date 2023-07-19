text = input("Text: ")

# print grade level of text
def grade(l, s):
    coleman = round(0.0588 * l - 0.296 * s - 15.8)
    if coleman < 1:
        print("Before Grade 1")
    elif coleman > 16:
        print("Grade 16+")
    else:
        print("Grade", coleman)

# calculate average number of letters per 100 words
def get_l(text):
    # get total number of letters in text
    l = 0
    for char in text:
        if char.isalpha():
            l += 1
    # find average number of letters per word
    l /= len(text.split())
    # return average number per 100 words
    return l * 100

# calculate average number of sentences per 100 words
def get_s(text):
    # get total number of sentences in text
    s = 0
    for char in text:
        if char == "." or char == "!" or char == "?":
            s += 1
    # find average number of sentences per word
    s /= len(text.split())
    # return average number per 100 words
    return s * 100

grade(get_l(text), get_s(text))