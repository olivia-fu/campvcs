string = input("String: ")

# 2 ways to find the length
ctr = 0
for i in string:
    ctr = ctr + 1
print(ctr)

print(len(string))

# splicing strings
print(string[:3])
print(string[1:3])
print(string[3:])
print(string[-3:])

# combining or repeating strings
print(string[:3] + string[1:3] + string[3:])
print(string[:3] * 3)

# find the number of instances of the first letter
first = string[0]
ctr = 0
for i in string:
    if i == first:
        ctr = ctr + 1
print(ctr)

# print only even indices
for i in string:
    if i % 2 == 0:
        print(i, end="")