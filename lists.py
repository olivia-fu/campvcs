# types of lists
cat1 = input("Cat 1: ")
cat2 = input("Cat 2: ")
cat3 = input("Cat 3: ")
input_cats = [cat1, cat2, cat3]
print(input_cats)

animals = ["penguin", "platypus", "rhino", "penguin"]
numbers = [1,2,3,4,5]
mixed = [1, "penguin", 2, "platypus", 3.5]

# similarities to strings
print(len(animals))
print(animals[0])
print(mixed[:-1])
print(mixed[:4])

print(animals[0]+animals[2])
print(numbers * 2)

# adding or removing items
animals.append("echidna")
animals.append("pangolin")
animals.insert(0, "killer whales")
print(animals)

animals.remove("rhino")
animals.pop(2)
print(animals)

# combining lists
mentors = ["olivia", "ethan", "frederico"]
zoo = animals+mentors
print(zoo)

animals.extend(mentors)
print(animals)

animals2 = animals.copy()
print(animals2)

# lists counting
animals2.append("olivia")
animals2.append("olivia")

oliviactr = animals2.count("olivia")
print(oliviactr)

# lists sorting
zoo.sort()
print(zoo)

zoo.reverse()
print(zoo)

# checking existence
if "ammonites" in zoo:
    print("yes look here!")
elif "trilobites" not in zoo:
    print("phew that's a relief")