print("Hello World")
name = input("What's your name?\n")
print("Hello " + name)

x = int(input("Define x.\n"))
y = int(input("Define y.\n"))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

if True:
    print("true")
if False:
    print("false")

x = 0
while True:
    x = x + 1
    print(x)
    if x == 3:
        break
print(x)

print("$" * 5)

for i in range(1,2,10):
    x += i
    print(x)

x = 0
while True:
    x += 1
    print(x)
    if x >= 10:
        break
print(x)