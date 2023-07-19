string1 = input("string1: ")
string2 = input("string2: ")
string3 = input("string3: ")
string4 = input("string4: ")
string5 = input("string5: ")

lst = []
lst.append(string1) 
lst.append(string2)
lst.append(string3)
lst.append(string4)
lst.append(string5)

# 1. swap first and last item
temp = lst[len(lst)-1]
lst[len(lst)-1] = lst[0]
lst[0] = temp
print(lst)

# 2. remove duplicates
for word in lst:
    while lst.count(word) > 1:
        lst.remove(word)
print(lst)