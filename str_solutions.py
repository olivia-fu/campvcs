string = input("String: ")

#1.
print(len(string))

#2.
print(string[0], end="")
for i in string[1:]:
    if i == string[0]:
        print("*", end="")
    else:
        print(i, end="")
print("")

#3.
for i in range(len(string)):
    if i % 2 == 1:
        print(string[i], end="")
print("")