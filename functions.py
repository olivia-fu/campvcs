# def function_name(arguments):
def calculator(a, b):
    sum = a+b
    sub = a-b
    # get a*b
    # get a/b
    # return sum, sub, a*b, a/b

print(calculator(2, 5))

# # print a response
# def hello():
#     name = input("Name: ")
#     print("hello " + name)
# hello()

# # return a computation
# def sum(a, b):
#     return a+b

# z = sum(3, 5)
# print(sum(z, 2))

# # return a boolean (true or false)
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# # 2 ways to compute if palindrome
# def palindrome1(x):
#     left = 0
#     right = len(x) - 1

#     while right >= left:
#         if not x[right] == x[left]:
#             return False
#         left += 1
#         right -= 1
#     return True

# def palindrome2(x):
#     return x == x[::-1]

# # accept unspecified number of arguments
# def repeat(*args):
#     for i in args:
#         print(i)

# # fix a default argument value
# def speak(text, speaker="Olivia"):
#     print(text + ", said " + speaker)

# speak("hello")
# speak("why hello there", "Haze")
# speak(text="one last time!", speaker="Yejin")

# # return multiple values
# def calc(a, b):
#     add = a + b
#     sub = a - b
#     mult = a * b
#     div = a / b
#     return add, sub, mult, div

# # print(mult) will throw an error!
# ## because mult is only defined in the function
# print(calc(1,3))

# # nested function
# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# print(outer_fun(5, 10))

# # recursive function
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
    
# print(factorial(5))