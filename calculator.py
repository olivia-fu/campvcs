print("Olivia's calculator")

x = int(input("type a number"))
y = int(input("type a second number"))
cmd = input("what command")

if cmd == "add":
    print(x+y)
elif cmd == "subtract":
    print(x-y)
elif cmd == "multiply":
    print(x*y)
elif cmd == "divide":
    print(x/y)
else:
    print("error, try again")
