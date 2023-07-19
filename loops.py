hp = ["gryffindor", "slytherin", "ravenclaw", "hufflepuff"]
for house in hp:
    if house == "slytherin":
        continue
    print(house)

besthouse = "gryffindor"
for i in besthouse:
    print(i)

for i in range(3):
    for j in range(2):
        print(i,j)

x = 0
while True:
    x = x+1
    if x == 6:
        break
print(x)

for i in range(5):
    print("*" * i)