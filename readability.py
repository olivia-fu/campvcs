text = input("Text: ")

# print out the grade level
def grade(l, s):
    # compute the formula
    grade = round(0.0588 * l - 0.296 * s - 15.8)
    # if the grade level is <1, print Before Grade 1
    if grade < 1:
        print("Before Grade 1")
    # if the grade level is 16+, print Grade 16+
    elif grade > 16:
        print("Grade 16+")
    # otherwise, print Grade #
    else:
        print("Grade " + str(grade))

# calculate average number of letters per 100 words
def get_l(text):
    # count total number of letters in text
    l_ctr = 0
    # count total number of words in text
    w_ctr = 1
    for i in text:
        if i.isalpha():
            l_ctr += 1
        elif i == " ":
            w_ctr += 1
    # find average per word times 100
    return l_ctr / w_ctr * 100

# calculate average number of sentences per 100 words
def get_s(text):
    # count total number of sentences in text
    s_ctr = 0
    # count total number of words in text
    w_ctr = 1
    for i in text:
        if i == "." or i == "!" or i == "?":
            s_ctr += 1
        elif i == " ":
            w_ctr += 1
    # find average per word times 100
    return s_ctr / w_ctr * 100

grade(get_l(text), get_s(text))

# # alternate solution
# # calculate average number of letters per 100 words
# def get_l(text):
#     # get total number of letters in text
#     l = 0
#     for char in text:
#         if char.isalpha():
#             l += 1
#     # find average number of letters per word
#     l /= len(text.split())
#     # return average number per 100 words
#     return l * 100

# # calculate average number of sentences per 100 words
# def get_s(text):
#     # get total number of sentences in text
#     s = 0
#     for char in text:
#         if char == "." or char == "!" or char == "?":
#             s += 1
#     # find average number of sentences per word
#     s /= len(text.split())
#     # return average number per 100 words
#     return s * 100